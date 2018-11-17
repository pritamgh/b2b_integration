import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";

import { Container, Row, Col, Input, Button, Card, CardBody } from 'mdbreact';

import { auth } from "../../actions/accounts";


class Register extends Component {

    state = {
        email: '',
        password: '',
    }

    onSubmit = e => {
        e.preventDefault();
        if (this.state.password !== this.state.confirm_password) {
            alert("Password Doesn't Matched !")
        }
        this.props.register(this.state.email, this.state.password);
    }

    render() {
        if (this.props.isAuthenticated) {
            return <Redirect to="/" />
        }
        return(
            <Container>
            <section className="form-simple">
              <Row>
                <Col md="5">
                  <Card>
                    
                    <div className="header pt-3 grey lighten-2">
                      <Row className="d-flex justify-content-start">
                        <h3 className="deep-grey-text mt-3 mb-4 pb-1 mx-5">Register</h3>
                      </Row>
                    </div>
                    
                    <CardBody className="mx-4 mt-4">
                      <form onSubmit={this.onSubmit}>
                        <Input label="enter email" group type="text" validate
                          onChange={e => this.setState({email: e.target.value})} />
                        <Input label="enter password" group type="password" validate containerClass="mb-0"
                          onChange={e => this.setState({password: e.target.value})} />
                        <Input label="confirm password" group type="password" validate containerClass="mb-0"
                          onChange={e => this.setState({confirm_password: e.target.value})} />
                        <div className="text-center mb-4 mt-5">
                          <Button color="primary" type="submit" className="btn-block z-depth-2">
                          SignUp</Button>
                        </div>
                      </form>
                    </CardBody>

                  </Card>
                </Col>
              </Row>
            </section>
          </Container>
        );
    }
};

const mapStateToProps = state => {
    let errors = [];
    if (state.auth.errors) {
        errors = Object.keys(state.auth.errors).map(field => {
            return {field, message: state.auth.errors[field]};
        });
    }
    return {
        errors,
        isAuthenticated: state.auth.isAuthenticated
    };
}

const mapDispatchToProps = dispatch => {
    return {
        register: (email, password) => dispatch(auth.register(email, password)),
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(Register);