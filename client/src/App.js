import React from 'react';
import axios from 'axios'

import './App.css';

import { FilePicker } from 'react-file-picker';

const BulletList = props => {
    const numbers = props.data;
    if (numbers.length === 0) {
        return (<ul>
            <li key={0}>{"No matches found - you have the best deal"}</li>
        </ul>)
    }
    const listItems = numbers.map((number) =>
        <li key={number}>{
            number.split('\n').map((item, i) => {
                return <p key={i}>{item}</p>;
            })
        }</li>
    );
    return (
        <ul>{listItems}</ul>
    );
};

const process = data => {
    if (data == null) {
        return ["No data yet..."]
    }
    const arr = [];
    for (const k in data) {
        if (data.hasOwnProperty(k)) {
            arr.push([k, data[k]])
        }

    }
    arr.sort((a, b) => {
        return a[1] > b[1] ? 1 : -1
    });
    const result = [];
    for (const elt in arr) {
        const price = arr[elt][1][1];
        result.push(`Store: ${arr[elt][0]}\nDistance: ${arr[elt][1][2]} miles\nPrice: $${parseFloat(price).toFixed(2)}\n`);
    }
    console.log(result);
    return result;
};

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            data: null,
            price: 0,
            loading: false,
        };

        this.handleChange = this.handleChange.bind(this);
    }

    async getResponse(file) {
        let data = new FormData();
        data.append('image', file, file.fileName);

        const url = `http://localhost:5000?price=${this.state.price}`;
        return await axios.post(url, data, {
            headers: {
                'accept': 'application/json',
                'Accept-Language': 'en-US,en;q=0.8',
                'Content-Type': `multipart/form-data; boundary=${data._boundary}`,
            }
        });
    }

    handleChange(event) {
        this.setState({ price: event.target.value });
    }

    render() {
        return (
            <div className='App'>
                <div className='App-header'>
                    cHarmony Savings Tool
                </div>
                <label>
                    Price: $
                    <input type="Price" value={this.state.value} onChange={this.handleChange} />
                </label>
                <FilePicker
                    extensions={['jpg', 'png']}
                    onChange={async FileObject => {
                        this.setState({
                            data: null,
                            loading: true,
                        });
                        const response = await this.getResponse(FileObject);
                        this.setState({
                            data: response.data,
                            loading: false,
                        });
                        process(this.state.data);
                    }}
                    onError={errMsg => alert(errMsg)}>
                    <button>
                        Click to upload barcode
                    </button>
                </FilePicker>
                <div className='App-List'>
                    {this.state.loading
                        ? 'Loading...'
                        : this.state.data == null
                            ? ''
                            :
                            <>
                                {`${process(this.state.data).length} matches found:`}
                                <BulletList data={process(this.state.data)} />
                            </>
                    }
                </div>
            </div>
        );
    }
}

export default App;