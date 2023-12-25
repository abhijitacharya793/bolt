import React from 'react'
import { useState } from "react";

import {
  Button,
  IconButton,
  Typography,
} from "@material-tailwind/react";
import { BoltIcon, ChartBarIcon, Cog6ToothIcon, ExclamationTriangleIcon, EyeSlashIcon, HomeIcon, LinkIcon, QueueListIcon, XMarkIcon } from "@heroicons/react/24/solid";

export default function Sidenav() {
  const [openSidenav, setOpenSidenav] = useState(true);
  const pathName = window.location.pathname;

  return (
    <>
      <aside
        className={`bg-white shadow-sm ${openSidenav ? "translate-x-0" : "-translate-x-80"
          } fixed inset-0 z-50 my-4 ml-4 h-[calc(100vh-32px)] w-72 rounded-xl transition-transform duration-300 xl:translate-x-0 border border-blue-gray-100`}
      >
        <div
          className={`relative`}
        >
          <a href="/home" className="py-6 px-8 text-center flex items-center gap-4">
            <BoltIcon className="w-5 h-5 text-center text-gray-900" />
            <Typography
              variant="h6"
              color="blue-gray"
            >
              BOLT
            </Typography>
          </a>
          <IconButton
            variant="text"
            color="white"
            size="sm"
            ripple={false}
            className="absolute right-0 top-0 grid rounded-br-none rounded-tl-none xl:hidden"
            onClick={() => setOpenSidenav(false)}
          >
            <XMarkIcon strokeWidth={2.5} className="h-5 w-5 text-white" />
          </IconButton>
        </div>
        <div className="m-4">
          <ul key="key" className="mb-4 flex flex-col gap-1">

            <li className="mx-3.5 mt-4 mb-2">
              <Typography
                variant="small"
                color="blue-gray"
                className="font-black uppercase opacity-75 text-sm font-semibold"
              >
                stats
              </Typography>
            </li>

            <li key="home">
              <a href="/home">
                <Button
                  variant={pathName === "/home" ? "gradient" : "text"}
                  color={
                    pathName === "/home"
                      ? "dark"
                      : "blue-gray"
                  }
                  className="flex items-center gap-4 px-4 capitalize"
                  fullWidth
                >
                  <HomeIcon className="w-4 h-4 text-inherit" />
                  <Typography
                    color="inherit"
                    className="font-medium capitalize text-sm font-semibold"
                  >
                    home
                  </Typography>
                </Button>
              </a>
            </li>
            <li key="dashboard">
              <a href="/dashboard">
                <Button
                  variant={pathName === "/dashboard" ? "gradient" : "text"}
                  color={
                    pathName === "/dashboard"
                      ? "dark"
                      : "blue-gray"
                  }
                  className="flex items-center gap-4 px-4 capitalize"
                  fullWidth
                >
                  <ChartBarIcon className="w-4 h-4 text-inherit" />
                  <Typography
                    color="inherit"
                    className="font-medium capitalize text-sm font-semibold"
                  >
                    dashboard
                  </Typography>
                </Button>
              </a>
            </li>

            <li className="mx-3.5 mt-4 mb-2">
              <Typography
                variant="small"
                color="blue-gray"
                className="font-black uppercase opacity-75 text-sm font-semibold"
              >
                apps
              </Typography>
            </li>

            <li key="adaptors">
              <a href="/adaptors">
                <Button
                  variant={pathName === "/adaptors" ? "gradient" : "text"}
                  color={
                    pathName === "/adaptors"
                      ? "dark"
                      : "blue-gray"
                  }
                  className="flex items-center gap-4 px-4 capitalize"
                  fullWidth
                >
                  <LinkIcon className="w-4 h-4 text-inherit" />
                  <Typography
                    color="inherit"
                    className="font-medium capitalize text-sm font-semibold"
                  >
                    adaptors
                  </Typography>
                </Button>
              </a>
            </li>
            <li key="scans">
              <a href="/scans">
                <Button
                  variant={pathName === "/scans" ? "gradient" : "text"}
                  color={
                    pathName === "/scans"
                      ? "dark"
                      : "blue-gray"
                  }
                  className="flex items-center gap-4 px-4 capitalize"
                  fullWidth
                >
                  <QueueListIcon className="w-4 h-4 text-inherit" />
                  <Typography
                    color="inherit"
                    className="font-medium capitalize text-sm font-semibold"
                  >
                    scans
                  </Typography>
                </Button>
              </a>
            </li>
            <li key="vulnerabilities">
              <a href="/vulnerabilities">
                <Button
                  variant={pathName === "/vulnerabilities" ? "gradient" : "text"}
                  color={
                    pathName === "/vulnerabilities"
                      ? "dark"
                      : "blue-gray"
                  }
                  className="flex items-center gap-4 px-4 capitalize"
                  fullWidth
                >
                  <ExclamationTriangleIcon className="w-4 h-4 text-inherit" />
                  <Typography
                    color="inherit"
                    className="font-medium capitalize text-sm font-semibold"
                  >
                    vulnerabilities
                  </Typography>
                </Button>
              </a>
            </li>
            <li key="secrets">
              <a href="/secrets">
                <Button
                  variant={pathName === "/secrets" ? "gradient" : "text"}
                  color={
                    pathName === "/secrets"
                      ? "dark"
                      : "blue-gray"
                  }
                  className="flex items-center gap-4 px-4 capitalize"
                  fullWidth
                >
                  <EyeSlashIcon className="w-4 h-4 text-inherit" />
                  <Typography
                    color="inherit"
                    className="font-medium capitalize text-sm font-semibold"
                  >
                    secrets
                  </Typography>
                </Button>
              </a>
            </li>

            <li className="mx-3.5 mt-4 mb-2">
              <Typography
                variant="small"
                color="blue-gray"
                className="font-black uppercase opacity-75 text-sm font-semibold"
              >
                configurations
              </Typography>
            </li>

            <li key="configurations">
              <a href="/configurations">
                <Button
                  variant={pathName === "/configurations" ? "gradient" : "text"}
                  color={
                    pathName === "/configurations"
                      ? "dark"
                      : "blue-gray"
                  }
                  className="flex items-center gap-4 px-4 capitalize"
                  fullWidth
                >
                  <Cog6ToothIcon className="w-4 h-4 text-inherit" />
                  <Typography
                    color="inherit"
                    className="font-medium capitalize text-sm font-semibold"
                  >
                    configurations
                  </Typography>
                </Button>
              </a>
            </li>

            <li className="mx-3.5 mt-4 mb-2">
              <Typography
                variant="small"
                color="blue-gray"
                className="font-black uppercase opacity-75 text-sm font-semibold"
              >
                socials
              </Typography>
            </li>

            <li key="twitter">
              <a href="/twitter">
                <Button
                  variant={pathName === "/twitter" ? "gradient" : "text"}
                  color={
                    pathName === "/twitter"
                      ? "dark"
                      : "blue-gray"
                  }
                  className="flex items-center gap-4 px-4 capitalize"
                  fullWidth
                >
                  <ChartBarIcon className="w-4 h-4 text-inherit" />
                  <Typography
                    color="inherit"
                    className="font-medium capitalize text-sm font-semibold"
                  >
                    twitter
                  </Typography>
                </Button>
              </a>
            </li>
          </ul>
        </div>
      </aside>
    </>
  )
}
