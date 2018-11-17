import React, { Component } from 'react';
import { connect } from "react-redux";
import axios from 'axios';

import { Fa, Button, Table, TableBody, TableHead } from 'mdbreact';

import {auth} from "../../actions/accounts";


class PurchaseOrders extends Component {

  constructor(props) {

    super(props);

    this.state = {
      podlist : [],
      podlinelist: [],
    };

    this.purchaseOrdersList = this.purchaseOrdersList.bind(this);
    this.purchaseOrderLineList = this.purchaseOrderLineList.bind(this);

  };

  purchaseOrderLineList(props) {

    var id = props.target.value;

    const endpoint = "http://127.0.0.1:8000/purchase-orders/header_id="+id+"/line-list/";

    axios.get(endpoint)
    .then((results)=>{
      //on success
      console.log(results.data);
      this.setState({
        podlinelist:results.data,
      });
    }).catch((error)=>{
      //on error
      alert(error);
    });

  };

  purchaseOrdersList() {

    // const endpoint = 'http://127.0.0.1:8000/api/purchase-orders/header-list/';
    const endpoint = 'http://127.0.0.1:8000/purchase-orders/header-list/';

    axios.get(endpoint)
    .then((results)=>{
      //on success
      this.setState({
        podlist:results.data,
      });
    }).catch((error)=>{
      //on error
      alert("There is an error in API call.");
    });

  };

  componentDidMount() {
    this.purchaseOrdersList();
  };

  render() {
    return (
      <div>
        <h4>Purchase Order Header List</h4>
        <div style={{textAlign: "right"}}>
          {this.props.user.email} (<a onClick={this.props.logout}>logout</a>)
        </div>
        <Table small bordered>
          <TableHead>
            <tr className="row">
              <th className="col-2"> Order Number </th>
              <th className="col-2"> Buyer Name </th>
              <th className="col-2"> Ship To Site </th>
              <th className="col-2"> Ship From Site </th>
              <th className="col-4"> Action </th>
            </tr>
          </TableHead>
          <TableBody>
            {this.state.podlist.map(item => (
              <tr className="row" key={item.header_id}>  
                <td className="col-2"> {item.order_number} </td>
                <td className="col-2"> {item.buyer_name} </td>
                <td className="col-2"> {item.ship_to_site} </td>
                <td className="col-2"> {item.ship_from_site} </td>
                <td className="col-4">
                  <Button onClick={this.purchaseOrderLineList} value={item.header_id} size="sm" color="info" rounded outline>
                    Info<Fa icon="info" className="ml-1"/>
                  </Button>
                  <Button value={item.header_id} size="sm" color="success" rounded outline>
                    Edit<Fa icon="edit" className="ml-1"/>
                  </Button>
                  <Button size="sm" color="danger" rounded outline>
                    Delete<Fa icon="trash" className="ml-1"/>
                  </Button>
                </td>
              </tr>
            ))}
          </TableBody>
        </Table>
        
        <h6>Purchase Order Line List</h6>

        {
          this.state.podlinelist !== undefined ? (
            <Table small>
              <TableHead>
                <tr>
                  <th> Line ID </th>
                  <th> Item </th>
                  <th> Unit of Measure </th>
                  <th> Price </th>
                  <th> Quantity </th>
                  <th> Action </th>
                </tr>
              </TableHead>
              <TableBody>               
                {this.state.podlinelist.map(item => (
                  <tr className="row-9" key={item.line_id}>  
                    <td> {item.line_id} </td>
                    <td> {item.item} </td>
                    <td> {item.uom} </td>
                    <td> {item.price} </td>
                    <td> {item.quantity} </td>
                    <td>
                      <Button onClick={this.purchaseOrderLineList} value={item.header_id} size="sm" color="info" rounded outline>
                        Details<Fa icon="info" className="ml-1"/>
                      </Button>
                      <Button value={item.line_id} size="sm" color="success" rounded outline>
                        Edit<Fa icon="edit" className="ml-1"/>
                      </Button>
                      <Button size="sm" color="danger" rounded outline>
                        Delete<Fa icon="trash" className="ml-1"/>
                      </Button>
                    </td>
                  </tr>
                ))}
              </TableBody>
            </Table>
          ) : (
            <h5>No lines found!</h5>
        )}

      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    user: state.auth.user,
  }
}

const mapDispatchToProps = dispatch => {
  return {
    logout: () => dispatch(auth.logout()),
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(PurchaseOrders);