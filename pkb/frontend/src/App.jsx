import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import DocumentList from './components/DocumentList';
import DocumentViewer from './components/DocumentViewer';

const App = () => {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <header className="bg-white shadow">
          <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
            <h1 className="text-3xl font-bold text-gray-900">
              Personal Knowledge Base
            </h1>
          </div>
        </header>
        <main>
          <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
            <Switch>
              <Route exact path="/" component={DocumentList} />
              <Route path="/document/:id" component={DocumentViewer} />
            </Switch>
          </div>
        </main>
      </div>
    </Router>
  );
}

export default App;
