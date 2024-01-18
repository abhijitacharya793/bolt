import React from "react";
import {
  Typography,
  Card,
  CardHeader,
  CardBody,
  IconButton,
  Menu,
  MenuHandler,
  MenuList,
  MenuItem,
  Avatar,
  Tooltip,
  Progress,
} from "@material-tailwind/react";
import StatisticsCard from "./dashboard/StatisticsCard";
import StatisticsChart from "./dashboard/StatisticsChart";

import { EllipsisVerticalIcon, ArrowUpIcon } from "@heroicons/react/24/outline";
import {
  BellIcon,
  CheckCircleIcon,
  ExclamationCircleIcon,
  ExclamationTriangleIcon,
  ListBulletIcon,
  NoSymbolIcon,
  ShieldExclamationIcon,
} from "@heroicons/react/24/solid";

export default function Home() {
  var number_of_issues = { critical: 1, high: 23, medium: 13, low: 40 };

  return (
    <>
      <div className="mt-12">
        <div className="mb-12 grid gap-y-10 gap-x-6 md:grid-cols-2 xl:grid-cols-5">
          <StatisticsCard
            icon={<ListBulletIcon className="h-6 w-6" />}
            entry="Total Scans"
            entry_value="30"
            change="-"
            change_value="55%"
            background="bg-blue-50"
            border="border-blue-500"
          />
          <StatisticsCard
            icon={<ExclamationCircleIcon className="h-6 w-6" />}
            entry="Critical"
            entry_value="1"
            change="+"
            change_value="55%"
            background="bg-red-50"
            border="border-red-500"
          />
          <StatisticsCard
            icon={<ExclamationTriangleIcon className="h-6 w-6" />}
            entry="High"
            entry_value="4"
            change="-"
            change_value="55%"
            background="bg-orange-50"
            border="border-orange-500"
          />
          <StatisticsCard
            icon={<ShieldExclamationIcon className="h-6 w-6" />}
            entry="Medium"
            entry_value="12"
            change="-"
            change_value="55%"
            background="bg-yellow-50"
            border="border-yellow-800"
          />
          <StatisticsCard
            icon={<NoSymbolIcon className="h-6 w-6" />}
            entry="Low"
            entry_value="55"
            change="-"
            change_value="55%"
            background="bg-green-50"
            border="border-green-500"
          />
        </div>
        <div className="mb-6 grid grid-cols-1 gap-y-12 gap-x-6 md:grid-cols-2 xl:grid-cols-3">
          <StatisticsChart />
          <StatisticsChart />
          <StatisticsChart />
        </div>
        <div className="mb-4 grid grid-cols-1 gap-6 xl:grid-cols-3">
          <Card className="overflow-hidden xl:col-span-2 border border-blue-gray-100 shadow-sm">
            <CardHeader
              floated={false}
              shadow={false}
              color="transparent"
              className="m-0 flex items-center justify-between p-6"
            >
              <div>
                <Typography variant="h6" color="blue-gray" className="mb-1">
                  Scans
                </Typography>
                <Typography
                  variant="small"
                  className="flex items-center gap-1 font-normal text-blue-gray-600"
                >
                  <CheckCircleIcon
                    strokeWidth={3}
                    className="h-4 w-4 text-blue-gray-200"
                  />
                  <strong>30 done</strong> this month
                </Typography>
              </div>
              <Menu placement="left-start">
                <MenuHandler>
                  <IconButton size="sm" variant="text" color="blue-gray">
                    <EllipsisVerticalIcon
                      strokeWidth={3}
                      fill="currenColor"
                      className="h-6 w-6"
                    />
                  </IconButton>
                </MenuHandler>
                <MenuList>
                  <MenuItem>Action</MenuItem>
                  <MenuItem>Another Action</MenuItem>
                  <MenuItem>Something else here</MenuItem>
                </MenuList>
              </Menu>
            </CardHeader>
            <CardBody className="overflow-x-scroll px-0 pt-0 pb-2">
              <table className="w-full min-w-[640px] table-auto">
                <thead>
                  <tr>
                    {["name", "number of issues", "hosts", "progress"].map(
                      (el) => (
                        <th
                          key={el}
                          className="border-b border-blue-gray-50 py-3 px-6 text-left"
                        >
                          <Typography
                            variant="small"
                            className="text-[11px] font-medium uppercase text-blue-gray-400"
                          >
                            {el}
                          </Typography>
                        </th>
                      )
                    )}
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td className="py-3 px-5 border-b border-blue-gray-50">
                      <div className="flex items-center gap-4">
                        <Typography
                          variant="small"
                          color="blue-gray"
                          className="font-bold"
                        >
                          FK_12/12/1223
                        </Typography>
                      </div>
                    </td>
                    <td className="py-3 px-5 border-b border-blue-gray-50 flex">
                      <Tooltip content={number_of_issues.critical}>
                        <div
                          className={`text-xs text-black cursor-pointer bg-red-100 py-1 px-2 mx-1 rounded-full border border-red-500`}
                        >
                          C
                        </div>
                      </Tooltip>
                      <Tooltip content={number_of_issues.high}>
                        <div
                          className={`text-xs text-black cursor-pointer bg-orange-100 py-1 px-2 mx-1 rounded-full border border-orange-500`}
                        >
                          H
                        </div>
                      </Tooltip>
                      <Tooltip content={number_of_issues.medium}>
                        <div
                          className={`text-xs text-black cursor-pointer bg-yellow-100 py-1 px-2 mx-1 rounded-full border border-yellow-500`}
                        >
                          M
                        </div>
                      </Tooltip>
                      <Tooltip content={number_of_issues.low}>
                        <div
                          className={`text-xs text-black cursor-pointer bg-green-100 py-1 px-2 mx-1 rounded-full border border-green-500`}
                        >
                          L
                        </div>
                      </Tooltip>
                    </td>
                    <td className="py-3 px-5 border-b border-blue-gray-50">
                      <Typography
                        variant="small"
                        className="text-xs font-medium text-blue-gray-600"
                      >
                        140
                      </Typography>
                    </td>
                    <td className="py-3 px-5 border-b border-blue-gray-50">
                      <div className="w-10/12">
                        <Typography
                          variant="small"
                          className="mb-1 block text-xs font-medium text-blue-gray-600"
                        >
                          50%
                        </Typography>
                        <Progress
                          value="50"
                          variant="gradient"
                          color="orange"
                          className="h-1"
                        />
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </CardBody>
          </Card>
          <Card className="border border-blue-gray-100 shadow-sm">
            <CardHeader
              floated={false}
              shadow={false}
              color="transparent"
              className="m-0 p-6"
            >
              <Typography variant="h6" color="blue-gray" className="mb-2">
                Orders Overview
              </Typography>
              <Typography
                variant="small"
                className="flex items-center gap-1 font-normal text-blue-gray-600"
              >
                <ArrowUpIcon
                  strokeWidth={3}
                  className="h-3.5 w-3.5 text-green-500"
                />
                <strong>24%</strong> this month
              </Typography>
            </CardHeader>
            <CardBody className="pt-0">
              <div key="title" className="flex items-start gap-4 py-3">
                <div
                  className={`relative p-1 after:absolute after:-bottom-6 after:left-2/4 after:w-0.5 after:-translate-x-2/4 after:bg-blue-gray-50 after:content-['']`}
                >
                  {React.createElement(BellIcon, {
                    className: `!w-5 !h-5 text-blue-gray-300`,
                  })}
                </div>
                <div>
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="block font-medium"
                  >
                    $2400, Design changes
                  </Typography>
                  <Typography
                    as="span"
                    variant="small"
                    className="text-xs font-medium text-blue-gray-500"
                  >
                    22 DEC 7:20 PM
                  </Typography>
                </div>
              </div>
              <div key="title" className="flex items-start gap-4 py-3">
                <div
                  className={`relative p-1 after:absolute after:-bottom-6 after:left-2/4 after:w-0.5 after:-translate-x-2/4 after:bg-blue-gray-50 after:content-['']`}
                >
                  {React.createElement(BellIcon, {
                    className: `!w-5 !h-5 text-blue-gray-300`,
                  })}
                </div>
                <div>
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="block font-medium"
                  >
                    $2400, Design changes
                  </Typography>
                  <Typography
                    as="span"
                    variant="small"
                    className="text-xs font-medium text-blue-gray-500"
                  >
                    22 DEC 7:20 PM
                  </Typography>
                </div>
              </div>
              <div key="title" className="flex items-start gap-4 py-3">
                <div
                  className={`relative p-1 after:absolute after:-bottom-6 after:left-2/4 after:w-0.5 after:-translate-x-2/4 after:bg-blue-gray-50 after:content-['']`}
                >
                  {React.createElement(BellIcon, {
                    className: `!w-5 !h-5 text-blue-gray-300`,
                  })}
                </div>
                <div>
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="block font-medium"
                  >
                    $2400, Design changes
                  </Typography>
                  <Typography
                    as="span"
                    variant="small"
                    className="text-xs font-medium text-blue-gray-500"
                  >
                    22 DEC 7:20 PM
                  </Typography>
                </div>
              </div>
              <div key="title" className="flex items-start gap-4 py-3">
                <div
                  className={`relative p-1 after:absolute after:-bottom-6 after:left-2/4 after:w-0.5 after:-translate-x-2/4 after:bg-blue-gray-50 after:content-['']`}
                >
                  {React.createElement(BellIcon, {
                    className: `!w-5 !h-5 text-blue-gray-300`,
                  })}
                </div>
                <div>
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="block font-medium"
                  >
                    $2400, Design changes
                  </Typography>
                  <Typography
                    as="span"
                    variant="small"
                    className="text-xs font-medium text-blue-gray-500"
                  >
                    22 DEC 7:20 PM
                  </Typography>
                </div>
              </div>
            </CardBody>
          </Card>
        </div>
      </div>
    </>
  );
}
