import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { createPosts } from '../action/postActions.js';


class PostForm extends Component {

	constructor(props) {
		super(props);
		this.state = {
			title: '',
			body: '' 
		};

		this.onChange = this.onChange.bind(this);
		this.onSubmit = this.onSubmit.bind(this);
	}

	onChange(e) {
		this.setState({ [e.target.name]: e.target.value });
	}

	onSubmit(e) {
		e.preventDefault();

		const post = {
			title: this.state.title,
			body: this.state.body
		};

		// call action
		this.props.createPosts(post);
	}

	render() {
		return(
			<div>
				<h1>Add Post</h1>
				<form onSubmit={this.onSubmit}>
					<input type='text' name='title' placeholder='enter title' 
					onChange={this.onChange} value={this.state.title} />
					<br/>
					<textarea name='body' placeholder='enter body' onChange={this.onChange}
					value={this.state.body} />
					<button type='submit'>post</button>
				</form>
			</div>
		)
	}
}

PostForm.propTypes = {
  createPosts: PropTypes.func.isRequired
};

export default connect(null, { createPosts })(PostForm);
