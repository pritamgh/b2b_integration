import { combineReducers } from 'redux';
import purchaseOrderReducer from './purchaseOrderReducer';

export default combineReducers({
	purchaseOrders: purchaseOrderReducer
})