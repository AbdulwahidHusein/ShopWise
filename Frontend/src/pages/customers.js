import axios from 'axios';
import { getAccessTokenCookie } from '../cookieUtils';
import Head from 'next/head';
import { useState, useEffect } from 'react';
import {
  Box,
  Button,
  Container,
  Pagination,
  Stack,
  SvgIcon,
  Typography,
  Grid
} from '@mui/material';
import { Layout as DashboardLayout } from 'src/layouts/dashboard/layout';
import { CompanyCard } from 'src/sections/companies/company-card';
import { CompaniesSearch } from 'src/sections/companies/companies-search';



const Page = () => {
  const [shopItems, setShopItems] = useState([]);


  useEffect(() => {
    const fetchData = async () => {
      try {
        const accessToken = getAccessTokenCookie();
        console.log(accessToken)
  
        const response = await axios.get(
          'http://127.0.0.1:8000/shops/get_all_items/',
          {
            headers: {
              Authorization: `Bearer ${accessToken}`,
            },
          }
        );
  
        console.log(response.data);
        if (response.data){
          setShopItems(response.data);
        }
         // Set the fetched data to the state
      } catch (error) {
        setShopItems([]);
        console.error('An error occurred while fetching items:', error);
      }
    };
  
    fetchData(); // Call the async function inside useEffect
  }, []); // Provide an empty dependency array to run the effect only once
  return (
    <>
      <Head>
        <title>My shop | Shopwise</title>
      </Head>
      <Box component="main" sx={{ flexGrow: 1, py: 8 }}>
        <Container maxWidth="xl">
          <Stack spacing={3}>
            <Stack direction="row" justifyContent="space-between" spacing={4}>
              <Stack spacing={1}>
                <Typography variant="h4">Virtual Shop</Typography>
                <Stack alignItems="center" direction="row" spacing={1}>
                  {/* Additional content */}
                </Stack>
              </Stack>
              <div>
                <Button variant="contained">List products</Button>
              </div>
            </Stack>
            <CompaniesSearch />
            <Grid container spacing={3}>
              {shopItems.map((data) => (
                <Grid item xs={12} md={6} lg={4} key={data.id}>
                  <CompanyCard item={data} />
                </Grid>
              ))}
            </Grid>
            <Box sx={{ display: 'flex', justifyContent: 'center' }}>
              <Pagination count={3} size="small" />
            </Box>
          </Stack>
        </Container>
      </Box>
    </>
  );
};

Page.getLayout = (page) => <DashboardLayout>{page}</DashboardLayout>;

export default Page;