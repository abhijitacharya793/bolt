import {
  ArrowRightCircleIcon,
  ArrowRightIcon,
  CheckBadgeIcon,
} from "@heroicons/react/24/solid";
import { BoltIcon } from "@heroicons/react/24/outline";

import {
  Avatar,
  Button,
  Card,
  CardBody,
  CardHeader,
  IconButton,
  Typography,
} from "@material-tailwind/react";
import React from "react";

export default function Status() {
  return (
    <div>
      <div className="flex">
        <div className="bg-red-50 w-1/2 rounded-lg shadow-md border border-red-500 text-center items-center">
          <div className="my-10 mx-4">
            <p className="pt-10 pb-10 uppercase font-bold text-black">
              Threat Level
            </p>
            <p className="py-10 text-6xl flex items-center justify-center">
              <BoltIcon className="w-14 h-14" /> Critical
            </p>
            <p className="mx-4 py-4 px-8 rounded-md bg-white">
              You should fix your critical severity issues immediately to avoid
              a breach.
            </p>
          </div>
        </div>
        <div className="w-2/3 pl-4">
          <div className="flex space-x-4 items-center rounded-md pr-4 bg-clip-border bg-gradient-to-tr from-gray-900 to-gray-800 text-white shadow-gray-900/20 shadow-lg">
            <div className="mx-4 my-2 w-2/3">
              <Typography
                variant="h5"
                color="white"
                className="text-base uppercase font-light"
              >
                Issues
              </Typography>
              <Typography variant="h1" color="white" className="font-light">
                309
              </Typography>
            </div>
            <a href="#" className="inline-block w-1/3">
              <Button
                size="sm"
                variant="text"
                className="flex items-center gap-2 text-white"
              >
                See all
                <ArrowRightIcon className="text-white w-4" />
              </Button>
            </a>
          </div>

          <div className="up flex items-center justify-center">
            <div className="bg-red-50 w-1/2 mt-4 mr-2 flex flex-col py-8 px-2 text-center rounded-md shadow-gray-900/20 shadow-md">
              <span className="uppercase pb-4">Critical</span>
              <span className="text-6xl">1</span>
            </div>
            <div className="bg-orange-50 w-1/2 mt-4 ml-2 flex flex-col py-8 px-2 text-center rounded-md shadow-gray-900/20 shadow-md">
              <span className="uppercase pb-4">High</span>
              <span className="text-6xl">4</span>
            </div>
          </div>
          <div className="down flex">
            <div className="bg-yellow-50 w-1/2 mt-4 mr-2 flex flex-col py-8 px-2 text-center rounded-md shadow-gray-900/20 shadow-md">
              <span className="uppercase pb-4">Medium</span>
              <span className="text-6xl">23</span>
            </div>
            <div className="bg-green-50 w-1/2 mt-4 ml-2 flex flex-col py-8 px-2 text-center rounded-md shadow-gray-900/20 shadow-md">
              <span className="uppercase pb-4">Low</span>
              <span className="text-6xl">122</span>
            </div>
          </div>
        </div>
      </div>
      <div className="bg-blue-50 rounded-lg shadow-md border border-blue-500 mt-4 p-4 flex items-center justify-start">
        <div className="pr-4">
          <CheckBadgeIcon className="w-10 h-10 text-green-500" />
        </div>
        <div className="">
          <p>Prominent issue</p>
          <p>There are no issues past their remediation date, good job!</p>
        </div>
      </div>
    </div>
  );
}
