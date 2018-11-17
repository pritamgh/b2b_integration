import React, {Component} from 'react';
import { connect } from "react-redux";
import { Link, Redirect } from "react-router-dom";

import { Container, Row, Col, Input, Button, Card, CardBody } from 'mdbreact';

import { auth } from "../../actions/accounts";


class Login extends Component  {

    state = {
        email: '',
        password: ''
    }

    onSubmit = e => {
        e.preventDefault();
        this.props.login(this.state.email, this.state.password);
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
                        <h3 className="deep-grey-text mt-3 mb-4 pb-1 mx-5">Log in</h3>
                        
                        {this.props.errors.length > 0 && (
                            <ul>
                                {this.props.errors.map(error => (
                                    <li key={error.field}>{error.message}</li>
                                ))}
                            </ul>
                        )}

                      </Row>
                    </div>
                    
                    <CardBody className="mx-4 mt-4">
                      <form onSubmit={this.onSubmit}>
                        <Input label="enter email" group type="text" validate
                          onChange={e => this.setState({email: e.target.value})} />
                        <Input label="enter password" group type="password" validate containerClass="mb-0"
                          onChange={e => this.setState({password: e.target.value})} />
                        <p className="font-small grey-text d-flex justify-content-end">
                          Forgot
                          <a href="#" className="dark-grey-text font-weight-bold ml-1">
                            Password?
                          </a>
                        </p>
                        <div className="text-center mb-4 mt-5">
                          <Button color="danger" type="submit" className="btn-block z-depth-2">
                          Log in</Button>
                        </div>
                      </form>
                      
                      <p className="font-small grey-text d-flex justify-content-center">
                        Don't have an account? 
                        <a className="dark-grey-text font-weight-bold ml-1">
                            <Link to="/register"> Sign up </Link>
                        </a>
                      </p>
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
        login: (email, password) => {
            return dispatch(auth.login(email, password));
        }
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(Login);