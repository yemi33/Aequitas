from unittest import result
from django.core.files import File
from django.http import HttpResponse, FileResponse, JsonResponse
from django.shortcuts import render
import os
import sys
import json
from api.aequitas.utils import *
from api.models import AequitasJob

def sendColumnNames(request):
  jobId = request.GET['jobId']
  job = AequitasJob.objects.get(id=jobId)
  result_directory = job.result_directory
  datasetName = job.dataset_name
  
  columnNames = get_column_names(f'{result_directory}/{datasetName}')

  response = JsonResponse({'status': 'Success',
                           'submittedFile': datasetName,
                           'jobId': jobId,
                           'columnNames': columnNames})
  return response

def updateConfig(request):
    jobId = request.POST['jobId']
    email = request.POST['email']
    
    job = AequitasJob.objects.get(id=jobId)
    job.owner_email = email # update user email
    job.save()
    
    return HttpResponse(job.owner_email)

def configureAequitas(request):
    if request.method == 'GET':
      return sendColumnNames(request)

    if request.method == 'POST':
      if 'email' in request.POST: # if it's an update request
        return updateConfig(request)
      
      jobId = request.POST['jobId']
      # if jobId != 1: 
      job = AequitasJob.objects.get(id=jobId)
      dataset_name = request.POST['filename']
      job.dataset_name = dataset_name
      sensitive_param = request.POST['sensitiveParam']
      job.sensitive_param = sensitive_param
      job.col_to_be_predicted = request.POST['predictedCol']
      job.get_model = True if request.POST['getModel'] == "true" else False
      model_type = request.POST['modelType']
      job.model_type = model_type
      job.aequitas_mode = request.POST['aequitasMode']
      job.threshold = request.POST['threshold']
      job.perturbation_unit = 1
      job.sample = 100
      job.num_trials = 100
      job.global_iteration_limit = 100
      job.local_iteration_limit = 100
      
      result_directory = f'api/aequitas/result_{jobId}'
      dataset_dir = f"{result_directory}/{dataset_name}"
      job.dataset_dir = dataset_dir
      job.num_params = len(get_column_names(dataset_dir)) - 1 # exclude 'y' col
      job.sensitive_param_idx = get_idx_of_column(dataset_dir, sensitive_param)
      job.pkl_dir = f"{result_directory}/{dataset_name.split('.')[0]}_{model_type}_Original.pkl"
      job.improved_pkl_dir = f"{result_directory}/{dataset_name.split('.')[0]}_{model_type}_Improved.pkl"
      job.retraining_inputs = f"{result_directory}/{dataset_name.split('.')[0]}_Retraining_Dataset.csv"
      job.improvement_graph = f"{result_directory}/{dataset_name.split('.')[0]}_Fairness_Improvement.png"
      #job.improvement_graph = 'api/aequitas/result/employee_fairness_improvement.png'
      
      job.save()

      response = JsonResponse({'status': 'Success',
                               'submittedFile': dataset_name,
                               'id': job.id})
      return response
