import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const DocumentList = () => {
  const [documents, setDocuments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDocuments = async () => {
      try {
        const response = await axios.get('/api/documents');
        setDocuments(response.data);
      } catch (error) {
        console.error('Error fetching documents:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchDocuments();
  }, []);

  if (loading) {
    return <div className="text-center py-8">Loading documents...</div>;
  }

  return (
    <div className="bg-white shadow overflow-hidden sm:rounded-lg">
      <ul className="divide-y divide-gray-200">
        {documents.map((doc) => (
          <li key={doc.id}>
            <Link
              to={`/document/${doc.id}`}
              className="block hover:bg-gray-50 px-4 py-4 sm:px-6"
            >
              <div className="flex items-center justify-between">
                <div className="text-sm font-medium text-indigo-600 truncate">
                  {doc.title}
                </div>
                <div className="ml-2 flex-shrink-0 flex">
                  <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                    {doc.content_type}
                  </span>
                </div>
              </div>
              <div className="mt-2 flex justify-between">
                <div className="text-sm text-gray-500">
                  Last updated: {new Date(doc.updated_at).toLocaleString()}
                </div>
              </div>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DocumentList;
import React from 'react';

const DocumentList = () => {
  // Temporary mock data
  const documents = [
    {
      id: 1,
      title: 'First Document',
      content_type: 'Note',
      updated_at: new Date().toISOString()
    },
    {
      id: 2,
      title: 'Second Document',
      content_type: 'Article',
      updated_at: new Date().toISOString()
    }
  ];

  return (
    <div className="bg-white shadow overflow-hidden sm:rounded-lg">
      <ul className="divide-y divide-gray-200">
        {documents.map((doc) => (
          <li key={doc.id}>
            <a
              href={`/document/${doc.id}`}
              className="block hover:bg-gray-50 px-4 py-4 sm:px-6"
            >
              <div className="flex items-center justify-between">
                <div className="text-sm font-medium text-indigo-600 truncate">
                  {doc.title}
                </div>
                <div className="ml-2 flex-shrink-0 flex">
                  <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                    {doc.content_type}
                  </span>
                </div>
              </div>
              <div className="mt-2 flex justify-between">
                <div className="text-sm text-gray-500">
                  Last updated: {new Date(doc.updated_at).toLocaleString()}
                </div>
              </div>
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DocumentList;
