import React, {Component} from 'react';
import Form from './pod_createForm'

import { Container, Row, Col, Card } from 'mdbreact';


class PurchaseOrderCreate extends Component {
	render() {
		return(
			<Container>
		        <section className="form-simple">
		          <Row>
		            <Col md="5">
						<Form />
					</Col>
				  </Row>
				</section>
			</Container>
		)
	}
}

export default PurchaseOrderCreate;