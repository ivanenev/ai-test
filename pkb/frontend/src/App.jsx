import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import DocumentList from './components/DocumentList';
import DocumentViewer from './components/DocumentViewer';

const App = () => {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <nav className="bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex">
                <div className="flex-shrink-0 flex items-center">
                  <Link to="/" className="text-xl font-bold text-blue-600">
                    Knowledge Base
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </nav>

        <main className="container mx-auto p-8">
          <Routes>
            <Route path="/" element={<DocumentList />} />
            <Route path="/document/:id" element={<DocumentViewer />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
