import React, {Component} from 'react'
//import FromControl from '@material-ui/core/Button';

class PurchaseOrderCreate extends Component {
	createPurchaseOrder() {
	    const endpoint = 'http://127.0.0.1:8000/api/purchase-orders/create/';
       
        let data = {
        	"order-number": "",
        	"order-type": "",
        	"payment-term": "",
        	"customer": "",
        	"supplier": "",
        	"buyer-name": "",
        	"order-date": "",
        	"currency": "",
        	"freight-term": "",
        	"ship-to-site": "",
        	"ship-from-site": "",
        }

	    let lookupOptions = {
	      method: 'POST',
	      headers: {
	        'Content-Type': 'application/json'
	      },
	      body: JSON.stringify(data)
	    }

	    fetch(endpoint, lookupOptions)
	    .then(function (response) {
	      return response.json()
	    }).then(function(responseData){
	      console.log(responseData)
	    }).catch(function(error){
	      console.log("error",error)
	    })
    }
	render() {
		return(
			<div id=''>
				<from>
					<input type='text' name='' placeholder='enter order number' />
					<input type='text' name='' placeholder='enter order type' />
					<input type='text' name='' placeholder='enter payment term' />
					<input type='text' name='' placeholder='enter customer' />
					<input type='text' name='' placeholder='enter supplier' />
					<input type='text' name='' placeholder='enter buyer name' />
					<input type='date' name='' placeholder='enter order date' />
					<input type='text' name='' placeholder='enter currency' />
					<input type='text' name='' placeholder='enter freight term' />
					<input type='text' name='' placeholder='enter ship to site' />
					<input type='text' name='' placeholder='enter ship from site' />
					<button type='submit' >submit</button>
				</from>
			</div>
		)
	}
}

export default PurchaseOrderCreate;