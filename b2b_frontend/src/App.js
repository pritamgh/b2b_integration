import React, { Component } from 'react';
import { Provider } from 'react-redux';

import PurchaseOrders from './components/purchase_orders/purchaseorders.js';
//import PurchaseOrderCreate from './components/purchase_orders/purchaseorder-create.js';
import store from './store.js';


class PurchaseOrdersApp extends Component {

  render() {
    return (
      <Provider store={store}>
        <div className="PurchaseOrdersApp">
          <PurchaseOrders />
        </div>
      </Provider>
    );
  }

}

export default PurchaseOrdersApp;