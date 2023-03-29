import React from 'react';
import  './App.css';
import Navigator from "./components/nav";
import RichText from './components/RichText'

export default class Table extends React.Component {
    render() {
        return <div>
            <header><Navigator/></header><div className="row">
                <div className="col-1"></div>
                <div className="col-2"><RichText /></div>
            <div className="col-1"></div>

        </div>
        </div>;
            
           
    }
}