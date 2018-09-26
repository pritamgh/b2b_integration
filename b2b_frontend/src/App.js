import React, { Component } from 'react';

import Search from './components/purchase_orders/search.js';
import PurchaseOrders from './components/purchase_orders/pod_list.js';
import PurchaseOrderCreate from './components/purchase_orders/pod_create.js';


class PurchaseOrdersApp extends Component {

  render() {
    return (
        <div className="PurchaseOrdersApp">
        	<div className="container" style={{'margin-top': '50px'}}>
        		<PurchaseOrders />
        	</div>
        	<div className="container" style={{'margin-top': '30px'}}>
            	<PurchaseOrderCreate />
            </div>
        </div>
    );
  }

}

export default PurchaseOrdersApp;