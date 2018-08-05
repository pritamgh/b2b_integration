import { FETCH_PURCHASE_ORDERS } from '../action/types.js';

const initialState = {
	items: [],
	item: {}
};

export default function(state= initialState, action) {
	switch (action.type) {
		case FETCH_PURCHASE_ORDERS:
			return {
				...state,
				items: action.payload
			};
		default:
			return state;
	}
}