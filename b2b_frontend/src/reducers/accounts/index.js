import { combineReducers } from 'redux';
// import notes from "./notes";
import auth from "./auth";


const B2BApp = combineReducers({
    auth,
})

export default B2BApp;
