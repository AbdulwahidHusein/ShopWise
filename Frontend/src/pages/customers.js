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


const companies = [
  {
    id: '2569ce0d517a7f06d3ea1f24',
    
    createdAt: '27/03/2019',
    description: 'Dropbox is a file hosting service that offers cloud storage, file synchronization, a personal cloud.',
    logo: '/assets/logos/logo-dropbox.png',
    title: 'Dropbox',
    downloads: '594'
  },
  {
    id: 'ed2b900870ceba72d203ec15',
    createdAt: '31/03/2019',
    description: 'Medium is an online publishing platform developed by Evan Williams, and launched in August 2012.',
    logo: '/assets/logos/logo-medium.png',
    title: 'Medium Corporation',
    downloads: '625'
  },
  {
    id: 'a033e38768c82fca90df3db7',
    createdAt: '03/04/2019',
    description: 'Slack is a cloud-based set of team collaboration tools and services, founded by Stewart Butterfield.',
    logo: '/assets/logos/logo-slack.png',
    title: 'Slack',
    downloads: '857'
  },
  {
    id: '1efecb2bf6a51def9869ab0f',
    createdAt: '04/04/2019',
    description: 'Lyft is an on-demand transportation company based in San Francisco, California.',
    logo: '/assets/logos/logo-lyft.png',
    title: 'Lyft',
    downloads: '406'
  },
  {
    id: '1ed68149f65fbc6089b5fd07',
    createdAt: '04/04/2019',
    description: 'GitHub is a web-based hosting service for version control of code using Git.',
    logo: '/assets/logos/logo-github.png',
    title: 'GitHub',
    downloads: '835'
  },
  {
    id: '5dab321376eff6177407e887',
    createdAt: '04/04/2019',
    description: 'Squarespace provides software as a service for website building and hosting. Headquartered in NYC.',
    logo: '/assets/logos/logo-squarespace.png',
    title: 'Squarespace',
    downloads: '835'
  }
];

const Page = () => {
  const [shopItems, setShopItems] = useState(null);


  useEffect(
    ()=>{
      const response = fetch('http://127.0.0.1:8000/accounts/login/', {
        method: 'POST',
        body: {}
      });

      if (response.ok) {
        const data = response.json();

      }
    }
  )

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
                <Button
                  variant="contained"
                >
                  List products
                </Button>
              </div>
            </Stack>
            <CompaniesSearch />
            <Grid container spacing={3}>
              {companies.map((company) => (
                <Grid xs={12} md={6} lg={4} key={company.id}>
                  <CompanyCard company={company} />
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