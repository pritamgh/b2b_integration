import React, { Component } from 'react';
import axios from 'axios';


class PurchaseOrderLine extends Component {

  constructor(props) {

    super(props);

    this.state = {
      podlinelist : [],
    };

    this.handleChangeHeaderID = this.handleChangeOrderNum.bind(this);

  };

  handleChangeHeaderID = event => {
      this.setState({order_number: event.target.value});
  };

  purchaseOrderLineList() {

    const endpoint = 'http://127.0.0.1:8000/purchase-orders/header_id=(?P<pk>[0-9]+)/line-list/';

    axios.get(endpoint)
    .then((results)=>{
      //on success
      this.setState({
        podlinelist:results.data,
      });
    }).catch((error)=>{
      //on error
      alert("There is an error in API call.");
    });
  }

  componentDidMount() {
    this.purchaseOrderLineList();
  }

}

export default PurchaseOrderLine;