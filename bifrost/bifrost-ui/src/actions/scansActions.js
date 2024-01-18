import { GET_SCANS, SCANS_ERROR } from "../types";
import axios from "axios";

export const getScans = () => async (dispatch) => {
  try {
    const res = await axios.get(`http://jsonplaceholder.typicode.com/scans`);
    dispatch({
      type: GET_SCANS,
      payload: res.data,
    });
  } catch (e) {
    dispatch({
      type: SCANS_ERROR,
      payload: console.log(e),
    });
  }
};
