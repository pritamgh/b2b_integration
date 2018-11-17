import React, { Component } from 'react';
import cookie from 'react-cookies';
import 'whatwg-fetch';
import Input from '@material-ui/core/Input';
import Button from '@material-ui/core/Button';


class Search extends Component {

    constructor(props) {

        super(props);

        this.state = {
            search_query: '',
        };

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChangeQuery = this.handleChangeQuery.bind(this);

    };


    handleChangeQuery = event => {
        this.setState({search_query: event.target.value});
    };

    handleSubmit = event => {

        event.preventDefault();

        const endpoint = 'http://127.0.0.1:8000/api/purchase-orders/search/';
        const csrfToken = cookie.load('csrftoken');
        
        let query = {
            "search_query": this.state.search_query,
        };
        console.log(query);

        //if (csrfToken !== undefined) {
            alert("Yessss");
            let lookupOptions = {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify(query),
                credentials: 'include'
            }
            fetch(endpoint, lookupOptions)
            .then(function(response) {
                // body...
                return response.json()
            }).then(function(responseData) {
                console.log(query)
            }).catch(function(error){
                console.log("error", error)
            })
        //}
    }

    
    render() {
        return (
          <form onSubmit={this.handleSubmit}>
            <div>
                <Input type='text' name='search_query' placeholder='enter ship from site' 
                 value={this.state.value} onChange={this.handleChangeQuery} />
            </div>
            <Button type="submit" variant="contained" color="secondary">
                Search
            </Button>
          </form>
        );
    }
}

export default Search;
