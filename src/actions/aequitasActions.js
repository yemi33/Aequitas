import Axios from 'axios';
import {
  DELETE_AEQUITAS_RESULT_FAIL,
  DELETE_AEQUITAS_RESULT_REQUEST,
  DELETE_AEQUITAS_RESULT_SUCCESS,
  GET_AEQUITAS_RESULT_FAIL,
  GET_AEQUITAS_RESULT_PENDING,
  GET_AEQUITAS_RESULT_REQUEST,
  GET_AEQUITAS_RESULT_SUCCESS,
  RUN_AEQUITAS_FAIL,
  RUN_AEQUITAS_REQUEST,
  RUN_AEQUITAS_SUCCESS
} from '../constants/aequitasConstants';
import WorkerBuilder from './workerBuilder';
import AequitasWorker from './aequitasWorker.js';

export const runAequitas = (jobId) => async (dispatch, getState) => {
  dispatch({
    type: RUN_AEQUITAS_REQUEST,
    payload: {
      jobId: jobId,
    },
  });
  try {
    // https://javascript.plainenglish.io/web-worker-in-react-9b2efafe309c
    // const worker = new WorkerBuilder(AequitasWorker);
    // worker.onerror = (e) => { console.log(e) };
    // worker.postMessage({ jobId });
    // worker.onmessage = (e) => {
    //   if (e) {
    //     dispatch({ type: RUN_AEQUITAS_SUCCESS, payload: e.data });
    //     worker.terminate();
    //   }
    // }
    // https://stackoverflow.com/questions/52372516/fetch-in-a-web-worker-using-react
    // axios doesn't work within web workers because of different scopes
    const { data } = await Axios.get(`/api/run?jobId=${jobId}`);
    if (data) {
      dispatch({ type: RUN_AEQUITAS_SUCCESS, payload: data });
    }
  } catch (error) {
    const message =
      error.response && error.response.data.message
        ? error.response.data.message
        : error.message;
    dispatch({ type: RUN_AEQUITAS_FAIL, payload: message });
  }
}

export const getAequitasResult = (jobId) => async (dispatch, getState) => {
  dispatch({
    type: GET_AEQUITAS_RESULT_REQUEST,
    payload: {
      jobId: jobId,
    },
  });
  try {
    const { data } = await Axios.get(
      `/api/getresult?jobId=${jobId}`
    );
    if (data.status === 'Pending') {
      dispatch({ type: GET_AEQUITAS_RESULT_PENDING, payload: data });
    } else {
      dispatch({ type: GET_AEQUITAS_RESULT_SUCCESS, payload: data });
    }
  } catch (error) {
    const message =
      error.response && error.response.data.message
        ? error.response.data.message
        : error.message;
    dispatch({ type: GET_AEQUITAS_RESULT_FAIL, payload: message });
  }
};

export const deleteAequitasResult = (jobId) => async (dispatch, getState) => {
  dispatch({
    type: DELETE_AEQUITAS_RESULT_REQUEST,
    payload: {
      jobId: jobId,
    }
  });
  try {
    const { data } = await Axios.get(
      `/api/deleteresult?jobId=${jobId}`
    );
    dispatch({ type: DELETE_AEQUITAS_RESULT_SUCCESS, payload: data });
  } catch (error) {
    const message =
      error.response && error.response.data.message
        ? error.response.data.message
        : error.message;
    dispatch({ type: DELETE_AEQUITAS_RESULT_FAIL, payload: message });
  }
}
