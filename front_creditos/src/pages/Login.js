import React, { useState } from 'react';
import { Box, Button, FormControl, FormLabel, Input,  createToaster } from '@chakra-ui/react';
import { login } from '../services/authService';

const Login = ({ setToken }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const toast = useToast();

  const handleLogin = async () => {
    try {
      const data = await login(username, password);
      setToken(data.token);
      localStorage.setItem('token', data.token);
      toast({
        title: "Inicio de sesión exitoso.",
        status: "success",
        duration: 2000,
        isClosable: true,
      });
    } catch (error) {
      toast({
        title: "Error en el inicio de sesión.",
        description: error.error || "Intente nuevamente.",
        status: "error",
        duration: 3000,
        isClosable: true,
      });
    }
  };

  return (
    <Box width="300px" mx="auto" mt="100px">
      <FormControl>
        <FormLabel>Username</FormLabel>
        <Input value={username} onChange={(e) => setUsername(e.target.value)} />
      </FormControl>
      <FormControl mt="4">
        <FormLabel>Password</FormLabel>
        <Input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </FormControl>
      <Button mt="6" colorScheme="blue" width="full" onClick={handleLogin}>
        Iniciar sesión
      </Button>
    </Box>
  );
};

export default Login;
