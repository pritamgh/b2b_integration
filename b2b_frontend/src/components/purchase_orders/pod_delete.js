import React, {Component} from 'react';
import PurchaseOrders from './pod_list'

import { Container, Row, Col, Card } from 'mdbreact';


class PurchaseOrderDelete extends Component {
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