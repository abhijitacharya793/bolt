import { GET_SCANS } from "../types";

const initialState = {
  scans: [],
  loading: true,
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_SCANS:
      return {
        ...state,
        scans: action.payload,
        loading: false,
      };
    default:
      return state;
  }
}
