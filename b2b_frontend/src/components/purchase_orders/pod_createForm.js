import React, { Component } from 'react';
import cookie from 'react-cookies';
import 'whatwg-fetch';

import { Input, Button } from 'mdbreact';


class Form extends Component {

    constructor(props) {

        super(props);

        this.state = {
            order_number: '',
            // "order_type": "",
            // "payment_term": "",
            // "customer": "",
            // "supplier": "",
            buyer_name: '',
            // "order_date": "",
            // "currency": "",
            // "freight_term": "",
            // "ship_to_site": "",
            ship_from_site: '',
        };

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChangeOrderNum = this.handleChangeOrderNum.bind(this);
        this.handleChangeBuyerName = this.handleChangeBuyerName.bind(this);
        this.handleChangeShipFromSite = this.handleChangeShipFromSite.bind(this);

    };


    handleChangeOrderNum = event => {
        this.setState({order_number: event.target.value});
    };
    handleChangeBuyerName = event => {
        this.setState({buyer_name: event.target.value});
    };
    handleChangeShipFromSite = event => {
        this.setState({ship_from_site: event.target.value});
    };

    handleSubmit = event => {

        event.preventDefault();

        const endpoint = 'http://127.0.0.1:8000/api/purchase-orders/create/';
        const csrfToken = cookie.load('csrftoken');
        
        let form_data = {
            "order_number": this.state.order_number,
            // "order_type": "",
            // "payment_term": "",
            // "customer": "",
            // "supplier": "",
            "buyer_name": this.state.buyer_name,
            // "order_date": "",
            // "currency": "",
            // "freight_term": "",
            // "ship_to_site": "",
            "ship_from_site": this.state.ship_from_site,
        };
        // console.log({form_data});

        //if (csrfToken !== undefined) {
            // alert("Yessss");
            let lookupOptions = {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify(form_data),
                credentials: 'include'
            }
            fetch(endpoint, lookupOptions)
            .then(function(response) {
                // body...
                return response.json()
            }).then(function(responseData) {
                console.log(form_data)
            }).catch(function(error){
                console.log("error", error)
            })
        //}
    }

    
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <div className="grey-text">
                    <Input type='text' name='order_number' label='enter order number' 
                     value={this.state.value} onChange={this.handleChangeOrderNum} />
                    <Input type='text' name='buyer_name' label='enter buyer name' 
                     value={this.state.value} onChange={this.handleChangeBuyerName} />
                    <Input type='text' name='ship_from_site' label='enter ship from site'
                     value={this.state.value} onChange={this.handleChangeShipFromSite} />                 
                </div>
                <div className="text-center">
                    <Button type="submit" className="btn btn-outline-purple">
                        Submit<i className="fa fa-paper-plane-o ml-2"></i>
                    </Button>
                </div>
            </form>        
        );
    }
}

export default Form;