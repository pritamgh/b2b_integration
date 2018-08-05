import { FETCH_PURCHASE_ORDERS } from './types.js';

export const fetchPurchaseOrders = () => dispatch => {
	
	fetch('http://127.0.0.1:8000/api/purchase-orders/header-list/')
		.then(res => res.json())
		.then(purchase_orders => dispatch({
			type: FETCH_PURCHASE_ORDERS,
			payload: purchase_orders
		}));
}

/*export const createPurchaseOrder = postData => dispatch => {
	fetch('https://jsonplaceholder.typicode.com/posts', {
			method: 'POST',
			headers: {
				'content-type': 'application/json'
			},
			body: JSON.stringify(postData)
		})
		  .then(res => res.json())
		  .then(post =>
		      dispatch({
		        type: NEW_PURCHASE_ORDERS,
		        payload: post
		      })
	    );
}*/