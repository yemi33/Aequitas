/* eslint-disable no-undef */

// eslint-disable-next-line import/no-anonymous-default-export
const AequitasWorker = () => {
  // eslint-disable-next-line no-restricted-globals
  self.onmessage = (message) => { // hey, the first param has to be named 'message'; it CANNOT be renamed into 'event'; I learned it the hard way
    const messageData = message.data;
    const { jobId } = messageData;
    // https://stackoverflow.com/questions/52372516/fetch-in-a-web-worker-using-react
    // axios doesn't work within web workers because of different scopes
    fetch(`https://aequitasweb.herokuapp.com/api/run?jobId=${jobId}`).then(response => {
      const { data } = response;
      postMessage(data);
    });
  };
}

export default AequitasWorker;
