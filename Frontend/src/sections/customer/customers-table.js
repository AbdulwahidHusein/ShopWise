import PropTypes from 'prop-types';
import ArrowDownOnSquareIcon from '@heroicons/react/24/solid/ArrowDownOnSquareIcon';
import ClockIcon from '@heroicons/react/24/solid/ClockIcon';
import { Avatar, Box, Card, CardContent, Divider, Stack, SvgIcon, Typography } from '@mui/material';

export const CustomersTable = (props) => {
  const { company } = props;
  return (
  <>
  <Card
  sx={{
    display: 'flex',
    flexDirection: 'column',
    height: '100%'
  }}
>
  <CardContent>
    <Box
      sx={{
        display: 'flex',
        justifyContent: 'center',
        pb: 3
      }}
    >
      <Avatar
        src={company.logo}
        variant="square"
      />
    </Box>
    <Typography
      align="center"
      gutterBottom
      variant="h5"
    >
      {company.title}
    </Typography>
    <Typography
      align="center"
      variant="body1"
    >
      {company.description}
    </Typography>
  </CardContent>
  <Box sx={{ flexGrow: 1 }} />
  <Divider />
  <Stack
    alignItems="center"
    direction="row"
    justifyContent="space-between"
    spacing={2}
    sx={{ p: 2 }}
  >
    <Stack
      alignItems="center"
      direction="row"
      spacing={1}
    >
      <SvgIcon
        color="action"
        fontSize="small"
      >
        <ClockIcon />
      </SvgIcon>
      <Typography
        color="text.secondary"
        display="inline"
        variant="body2"
      >
        Added 2hr ago
      </Typography>
    </Stack>
    <Stack
      alignItems="center"
      direction="row"
      spacing={1}
    >
      <SvgIcon
        color="action"
        fontSize="small"
      >
        <ArrowDownOnSquareIcon />
      </SvgIcon>
      <Typography
        color="text.secondary"
        display="inline"
        variant="body2"
      >
        {company.downloads} Adds
      </Typography>
    </Stack>
  </Stack>
</Card>
</>)
};

CustomersTable.propTypes = {
  count: PropTypes.number,
  items: PropTypes.array,
  onDeselectAll: PropTypes.func,
  onDeselectOne: PropTypes.func,
  onPageChange: PropTypes.func,
  onRowsPerPageChange: PropTypes.func,
  onSelectAll: PropTypes.func,
  onSelectOne: PropTypes.func,
  page: PropTypes.number,
  rowsPerPage: PropTypes.number,
  selected: PropTypes.array
};
