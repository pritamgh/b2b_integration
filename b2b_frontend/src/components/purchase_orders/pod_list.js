import React, { Component } from 'react';
import axios from 'axios';

import { Fa, Button, Table, TableBody, TableHead } from 'mdbreact';
import PurchaseOrderLine from './podline_list';


class PurchaseOrders extends Component {

  constructor(props) {

    super(props);

    this.state = {
      podlist : [],
      podlinelist: [],
    };

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
    // this.purchaseOrderLineList();
  };

  render() {

    const { podlist } = this.state.podlist;
    const { podlinelist } = this.state.podlinelist;

    return (
      <div>
        <Table responsive hover bordered>
          <TableHead>
            <tr className="row">
              <th className="col-2"> Order Number </th>
              <th className="col-2"> Buyer Name </th>
              <th className="col-2"> Ship From Site </th>
              <th className="col-4"> Action </th>
            </tr>
          </TableHead>
          <TableBody>
            {this.state.podlist.map(item => (
              <tr className="row" key={item.header_id}>  
                <td className="col-2"> {item.order_number} </td>
                <td className="col-2"> {item.buyer_name} </td>
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
            ))};
          </TableBody>
        </Table>

        {
          podlinelist !== undefined ? (
            <Table responsive hover bordered>
              <TableHead>
                <tr className="row">
                  <th className="col-2"> Line ID </th>
                  <th className="col-2"> Item </th>
                  <th className="col-2"> Unit of Measure </th>
                  <th className="col-2"> Price </th>
                  <th className="col-2"> Quantity </th>
                  <th className="col-4"> Action </th>
                </tr>
              </TableHead>
              <TableBody>
                {podlinelist.map(item => (
                  <tr className="row" key={item.line_id}>  
                    <td className="col-2"> {item.line_id} </td>
                    <td className="col-2"> {item.item} </td>
                    <td className="col-2"> {item.uom} </td>
                    <td className="col-2"> {item.price} </td>
                    <td className="col-2"> {item.quantity} </td>
                    <td className="col-4">
                      <Button value={item.line_id} size="sm" color="info" rounded outline>
                        Info<Fa icon="info" className="ml-1"/>
                      </Button>
                      <Button value={item.line_id} size="sm" color="success" rounded outline>
                        Edit<Fa icon="edit" className="ml-1"/>
                      </Button>
                      <Button size="sm" color="danger" rounded outline>
                        Delete<Fa icon="trash" className="ml-1"/>
                      </Button>
                    </td>
                  </tr>
                ))};
              </TableBody>
            </Table>
          ) : (
            <h5>No lines found!</h5>
        )}

      </div>
    );
  }

}

export default PurchaseOrders;