import React, { useState } from 'react';
import { Button  } from '@mui/material';


function DatabaseHealthCheck() {
  const apiBase = '/api';
  const [message, setMessage] = useState('');

  const fetchData = () => {
    setMessage('')
    // Le fetch reste le même, mais vous devez vous préparer à recevoir un blob au lieu d'un JSON.
    fetch(`${apiBase}/neo4j_healthcheck`, {
        method: 'GET',
    })
    .then((response) => {
        if (response.ok) {
            // Vous devez renvoyer à la fois le blob et la réponse ici pour avoir accès aux en-têtes ensuite.
            setMessage('Neo4j is Running');
        } else {
          setMessage('Neo4j is not running');
        }
    })
    .catch((error) => {
        console.error('Error explaining code:', error);
        setMessage('An error as occured');
    });
  };

  return (
    <div
      style={{
        position: 'fixed',
        bottom: '50%',
        left: 0,
        right: 0,
        height: 0,
        maxWidth: '50%',
        margin: 'auto',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'flex-end',
        boxSizing: 'border-box',
      }}
    >
      <Button
        variant="outlined"
        color="secondary"
        size="large"
        onClick={() => fetchData()} // Appeler la fonction de suppression avec l'index
        style={{ marginLeft: '8px' }}
      >
        Test Neo4j Connexion
      </Button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default DatabaseHealthCheck;
