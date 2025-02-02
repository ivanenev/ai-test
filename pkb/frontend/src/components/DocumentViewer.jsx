import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import FeedbackAgent from './FeedbackAgent';

const DocumentViewer = () => {
  const { id } = useParams();
  const [document, setDocument] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchDocument = async () => {
      try {
        const response = await axios.get(`/api/documents/${id}`);
        setDocument(response.data);
      } catch (error) {
        console.error('Error fetching document:', error);
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchDocument();
  }, [id]);

  if (loading) {
    return <div className="text-center py-8">Loading document...</div>;
  }

  if (error) {
    return (
      <div className="text-center py-8 text-red-600">
        Error loading document: {error}
      </div>
    );
  }

  if (!document) {
    return <div className="text-center py-8">Document not found</div>;
  }

  return (
    <div className="bg-white shadow overflow-hidden sm:rounded-lg">
      <div className="px-4 py-5 sm:px-6">
        <h3 className="text-lg leading-6 font-medium text-gray-900">
          {document.title}
        </h3>
        <p className="mt-1 max-w-2xl text-sm text-gray-500">
          {document.content_type}
        </p>
      </div>
      <div className="border-t border-gray-200 px-4 py-5 sm:p-0">
        <dl className="sm:divide-y sm:divide-gray-200">
          <div className="py-4 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
            <dt className="text-sm font-medium text-gray-500">Content</dt>
            <dd className="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
              <pre className="whitespace-pre-wrap">{document.content}</pre>
            </dd>
          </div>
        </dl>
      </div>
      <div className="px-4 py-5 sm:px-6">
        <FeedbackAgent documentId={id} />
      </div>
    </div>
  );
};

export default DocumentViewer;
