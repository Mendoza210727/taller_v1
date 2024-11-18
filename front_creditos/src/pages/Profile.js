import React, { useEffect, useState } from 'react';
import { Box, Text, Spinner, useToast } from '@chakra-ui/react';
import { fetchProfile } from '../services/authService';

const Profile = ({ token }) => {
  const [profile, setProfile] = useState(null);
  const toast = useToast();

  useEffect(() => {
    const loadProfile = async () => {
      try {
        const data = await fetchProfile(token);
        setProfile(data);
      } catch (error) {
        toast({
          title: "Error cargando el perfil.",
          description: error.error || "Intente nuevamente.",
          status: "error",
          duration: 3000,
          isClosable: true,
        });
      }
    };
    loadProfile();
  }, [token, toast]);

  if (!profile) return <Spinner />;

  return (
    <Box mt="50px" textAlign="center">
      <Text fontSize="xl">Nombre: {profile.username}</Text>
      <Text fontSize="lg">Email: {profile.email}</Text>
    </Box>
  );
};

export default Profile;
