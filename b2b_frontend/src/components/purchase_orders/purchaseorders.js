/*import React, { Component } from 'react';


class PurchaseOrders extends Component {

  state = {
    headers : []
  };

  async purchaseOrdersList() {
    try {
      const endpoint = await fetch('http://127.0.0.1:8000/api/purchase-orders/header-list/');
      const headers = await endpoint.json();
      this.setState({
        headers
      });
      console.log(headers);
    }
    catch (e) {
      console.log(e);
    }
  }

  componentDidMount() {
    this.purchaseOrdersList();
  }

  render() {
    return (
      <div>
        {this.state.headers.map(item => (
          <div key={item.header_id}>
            <h1>{item.buyer_name}</h1>
            <span>{item.ship_to_site}</span>
            <span>{item.ship_from_site}</span>
          </div>
        ))}
      </div>
    );
  }

}

export default PurchaseOrders;*/


import React, {Component} from 'react';
import { PropTypes } from 'prop-types';
import { connect } from 'react-redux';
import { fetchPurchaseOrders } from '../../action/purchaseOrderActions.js';


class PurchaseOrders extends Component {

  componentWillMount() {
    this.props.fetchPurchaseOrders();
  }

  componentWillReceiveProps(nextProps) {
      if (nextProps.newPurchaseOrder) {
        this.props.purchase_orders.unshift(nextProps.newPurchaseOrder);
      }
  }


  render() {
    const purchase_Orders = this.props.purchase_orders.map(purchase_order => (
      <div key={purchase_order.id}>
        <span>{purchase_order.ship_to_site}</span>
      </div>
    ));
    return(
      <div>
        <h1>Redux</h1>
        {purchase_Orders}
      </div>
    )
  }
}

// PurchaseOrders.propTypes = {
//   fetchPurchaseOrders: PropTypes.func.isRequired,
//   purchase_orders: PropTypes.array.isRequired,
//   //newPurchaseOrder: PropTypes.object
// };

// const mapStateToProps = state => ({
//   purchase_orders: state.purchase_orders.items
// });

// export default connect(mapStateToProps, {fetchPurchaseOrders})(PurchaseOrders);
export default PurchaseOrders;