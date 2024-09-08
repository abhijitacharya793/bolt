import React from "react";
import {
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  Typography,
} from "@material-tailwind/react";

import Chart from "react-apexcharts";
import { ClockIcon } from "@heroicons/react/24/solid";

export default function StatisticsChart() {
  const chartsConfig = {
    chart: {
      toolbar: {
        show: false,
      },
    },
    title: {
      show: "",
    },
    dataLabels: {
      enabled: false,
    },
    xaxis: {
      axisTicks: {
        show: false,
      },
      axisBorder: {
        show: false,
      },
      labels: {
        style: {
          colors: "#37474f",
          fontSize: "13px",
          fontFamily: "inherit",
          fontWeight: 300,
        },
      },
    },
    yaxis: {
      labels: {
        style: {
          colors: "#37474f",
          fontSize: "13px",
          fontFamily: "inherit",
          fontWeight: 300,
        },
      },
    },
    grid: {
      show: true,
      borderColor: "#dddddd",
      strokeDashArray: 5,
      xaxis: {
        lines: {
          show: true,
        },
      },
      padding: {
        top: 5,
        right: 20,
      },
    },
    fill: {
      opacity: 0.8,
    },
    tooltip: {
      theme: "dark",
    },
  };
  const websiteViewsChart = {
    type: "bar",
    height: 220,
    series: [
      {
        name: "Views",
        data: [50, 20, 10, 22, 50, 10, 40],
      },
    ],
    options: {
      ...chartsConfig,
      colors: "#388e3c",
      plotOptions: {
        bar: {
          columnWidth: "16%",
          borderRadius: 5,
        },
      },
      xaxis: {
        ...chartsConfig.xaxis,
        categories: ["M", "T", "W", "T", "F", "S", "S"],
      },
    },
  };

  return (
    <>
      <Card className="border border-blue-gray-100 shadow-sm">
        <CardHeader
          variant="gradient"
          color="white"
          floated={false}
          shadow={false}
        >
          <Chart {...websiteViewsChart} />
        </CardHeader>
        <CardBody className="px-6 pt-0">
          <Typography variant="h6" color="blue-gray">
            Website View
          </Typography>
          <Typography
            variant="small"
            className="font-normal text-blue-gray-600"
          >
            Last Campaign Performance
          </Typography>
        </CardBody>
        <CardFooter className="flex border-t border-blue-gray-50 px-6 py-5 font-sans text-sm items-center">
          <ClockIcon className="h-4 w-4 text-blue-gray-400" />
          &nbsp; campaign sent 2 days ago
        </CardFooter>
      </Card>
    </>
  );
}
