import React from 'react';
import { Router, Route } from 'react-router-dom';
import history from './history';

import Headlines from './components/News Page/Headlines'
import Headline from './components/News Page/Headline'
import HeadlineDetail from './components/News Page/HeadlineDetail';
import Navbar from './components/Navbar';

import Statistics from './components/Stats Page/Statistics'

import Events from './components/News & Economy Page/Events';
import Events2 from './components/News & Economy Page/Events2';
import 'bootstrap/dist/css/bootstrap.min.css';


const App = () => {
    return (<>
                <Router history = {history}>
                  <Route path = "/" component = {Navbar} />
                  <Route path = "/headlines" component = {Headlines}/>
                  <Route path = "/events" component = {Events}/>
                  <Route path = "/detail/:id" component = {HeadlineDetail}/>
                  <Route path = "/example" component = {Headline}/>
                  <Route path = "/stats" component = {Statistics}/> 
                </Router> 
            </>)
}

export default App;
