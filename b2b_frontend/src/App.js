import React, { Component } from 'react';
import { Route, Switch, BrowserRouter, Redirect } from 'react-router-dom';
import Img from 'react-image';

import { Provider, connect } from "react-redux";
import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";

import PurchaseOrders from './components/purchase_orders/pod_list.js';
// import PurchaseOrderCreate from './components/purchase_orders/pod_create.js';

import Search from './components/search/search.js';

// import NotFound from "./components/NotFound";
import Register from "./components/accounts/registration";
import Login from './components/accounts/login.js';

import { auth } from "./actions/accounts";
import B2BApp from "./reducers/accounts";


let store = createStore(B2BApp, applyMiddleware(thunk));


class PurchaseOrdersApp extends Component {

    componentDidMount() {
        this.props.loadUser();
    }

    PrivateRoute = ({component: ChildComponent, ...rest}) => {
        return <Route {...rest} render={props => {
            if (this.props.auth.isLoading) {
                // return <em>Loading...</em>;
                return <Img src="../public/spinner1.gif" />;
            } else if (!this.props.auth.isAuthenticated) {
                return <Redirect to="/login" />
            } else {
                return <ChildComponent {...props} />
            }
        }} />
    }

    render() {
        let {PrivateRoute} = this;
        return (
            <div className="container" style={{'marginTop': '50px'}}>
                <Provider store={store}>
                    <BrowserRouter>
                        <Switch>
                            <PrivateRoute exact path="/" component={PurchaseOrders} />
                            <Route exact path="/login" component={Login} /> <Route exact path="/register" component={Register} />
                        </Switch>
                    </BrowserRouter>
                </Provider>
            </div>
        );
    }
}

const mapStateToProps = state => {
    return {
        auth: state.auth,
    }
}

const mapDispatchToProps = dispatch => {
    return {
        loadUser: () => {
            return dispatch(auth.loadUser());
        }
    }
}

let RootContainer = connect(mapStateToProps, mapDispatchToProps)(PurchaseOrdersApp);


export default class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <RootContainer />
            </Provider>
        )
    }
}