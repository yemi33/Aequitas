import { createStore, compose, applyMiddleware, combineReducers } from "redux";
import thunk from "redux-thunk";
<<<<<<< HEAD
import { uploadDatasetReducer } from "./reducers/uploadDataset";

const reducer = combineReducers({
  uploadDataset: uploadDatasetReducer,
});

const initialState = {};
=======
import { aequitasRunReducer, getAequitasResultReducer, deleteAequitasResultReducer } from "./reducers/aequitasReducers";
import { downloadDatasetReducer, downloadModelReducer } from "./reducers/downloadReducers";
import { sendEmailReducer } from "./reducers/emailReducers";
import { configCreateReducer, configUpdateReducer, fileSubmitReducer } from "./reducers/submitReducers";

const initialState = {
};

const reducer = combineReducers({
  fileSubmit: fileSubmitReducer,
  aequitasRunResult: aequitasRunReducer,
  downloadDataset: downloadDatasetReducer,
  downloadModel: downloadModelReducer,
  configCreate: configCreateReducer,
  configUpdate: configUpdateReducer,
  sendEmail: sendEmailReducer,
  getAequitasResult: getAequitasResultReducer,
  deleteAequitasResult: deleteAequitasResultReducer,
})
>>>>>>> origin/yunping_packageversion

const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(
  reducer,
  initialState,
  composeEnhancer(applyMiddleware(thunk))
);

export default store;
