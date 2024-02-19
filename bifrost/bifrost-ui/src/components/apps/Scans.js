import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import {
  Accordion,
  AccordionHeader,
  AccordionBody,
} from "@material-tailwind/react";
import {
  Card,
  CardBody,
  CardHeader,
  CardFooter,
  Avatar,
  Typography,
  Tabs,
  TabsHeader,
  Tab,
  Tooltip,
  Progress,
  Chip,
  Button,
} from "@material-tailwind/react";
import {
  HomeIcon,
  ChatBubbleLeftEllipsisIcon,
  Cog6ToothIcon,
  QueueListIcon,
  EllipsisVerticalIcon,
  GlobeAsiaAustraliaIcon,
  LinkIcon,
  DevicePhoneMobileIcon,
  CloudIcon,
} from "@heroicons/react/24/solid";

export default function Asgard() {
  const [scans, setScans] = useState({});
  const [toggle, setToggle] = React.useState([]);

  const handleClick = (key) => {
    let newArr = [...toggle];
    newArr[key] = toggle[key] === 0 ? 1 : 0;
    setToggle(newArr);
  };
  // TODO: update to valhalla
  const getScans = () => {
    fetch("http://valhalla-api:8335/valhalla/v1/enricher/", {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => {
        const result = Object.groupBy(data, ({ scan_id }) => scan_id);
        setScans(result);
        setToggle(new Array(data.length).fill(0));
      })
      .catch((err) => console.error(err));
  };

  useEffect(() => {
    getScans();
  }, []);

  let navigate = useNavigate();
  const navigateToScanDetails = (e) => {
    console.log(e.target.name);
    navigate(`/scans/scandetails/${e.target.name}`);
  };

  return (
    <>
      <div className="relative mt-8 h-36 w-full overflow-hidden rounded-xl bg-cover bg-center">
        <div className="absolute inset-0 h-full w-full bg-red-100" />
      </div>

      <Card className="mx-3 -mt-16 mb-6 lg:mx-4 border border-blue-gray-100">
        <CardBody className="p-4">
          <div className="mb-10 flex items-center justify-between flex-wrap gap-6">
            <div className="flex items-center gap-6">
              <div className="rounded-lg blue border border-blue-gray-900 w-20 h-20 justify-center items-center flex">
                <QueueListIcon fill="blue-gray" className="w-8 h-8" />
              </div>
              <div>
                <Typography variant="h5" color="blue-gray" className="mb-1">
                  Scans
                </Typography>
                <Typography
                  variant="small"
                  className="font-normal text-blue-gray-600"
                >
                  Get an overview of all scans running and navigate your way to
                  vulnerabilities!
                </Typography>
              </div>
            </div>
            <div className="w-96">
              <Tabs value="app">
                <TabsHeader>
                  <Tab value="api">
                    <GlobeAsiaAustraliaIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                    Web/API
                  </Tab>
                  <Tab value="mobile">
                    <DevicePhoneMobileIcon className="-mt-0.5 mr-2 inline-block h-5 w-5" />
                    Mobile
                  </Tab>
                  <Tab value="cloud">
                    <CloudIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                    Cloud
                  </Tab>
                </TabsHeader>
              </Tabs>
            </div>
          </div>
          <div className="gird-cols-1 mb-12 grid gap-12 px-4">
            <Card>
              <CardHeader variant="gradient" color="gray" className="mb-8 p-6">
                <Typography variant="h6" color="white">
                  managed by <code className="text-red-100">asgard</code>
                </Typography>
              </CardHeader>
              <CardBody className="overflow-x-scroll px-0 pt-0 pb-2">
                {Object.keys(scans).map((scan_id, index) => {
                  return (
                    <Accordion
                      open={toggle[index] === 1}
                      className="m-4 rounded-lg border border-blue-gray-100 w-auto"
                    >
                      <AccordionHeader
                        onClick={() => handleClick(index)}
                        className={`border-b-0 transition-colors p-8 ${
                          toggle[index] === 1
                            ? "text-white hover:!text-gray-300 bg-gradient-to-tr from-gray-900 to-gray-800 rounded-lg"
                            : ""
                        }`}
                      >
                        <div className="flex items-center w-full text-base font-sans font-semibold leading-relaxed">
                          <span className="w-full flex ">
                            {scan_id} &nbsp;|&nbsp; this scan has&nbsp;
                            <p
                              className={` ${
                                toggle[index] === 1
                                  ? "text-red-100"
                                  : "text-red-600"
                              }`}
                            >
                              {scans[scan_id].length}
                            </p>
                            &nbsp;apis
                          </span>
                          <div className="justify-end">
                            <div className="flex items-center gap-4">
                              <Button
                                name={scan_id}
                                onClick={navigateToScanDetails}
                                color={`${
                                  toggle[index] === 1 ? "white" : "black"
                                }`}
                              >
                                details
                              </Button>
                            </div>
                          </div>
                        </div>
                      </AccordionHeader>
                      <AccordionBody>
                        <table className="w-full min-w-[640px] table-auto m-3">
                          <thead>
                            <tr>
                              {[
                                "Sr. No.",
                                "scope",
                                "power",
                                "completion",
                                "triggered",
                                "",
                              ].map((el) => (
                                <th
                                  key={el}
                                  className="border-b border-blue-gray-50 py-3 px-5 text-left"
                                >
                                  <Typography
                                    variant="small"
                                    className="text-[11px] font-bold uppercase text-blue-gray-400"
                                  >
                                    {el}
                                  </Typography>
                                </th>
                              ))}
                            </tr>
                          </thead>
                          <tbody>
                            {scans[scan_id].map(
                              (
                                {
                                  id,
                                  scan_id,
                                  scope,
                                  power,
                                  completion,
                                  tasks,
                                  triggered,
                                  uuid,
                                },
                                key
                              ) => {
                                const className = `py-3 px-5 ${
                                  key === scans.length - 1
                                    ? ""
                                    : "border-b border-blue-gray-50"
                                }`;
                                return (
                                  <tr key={scan_id}>
                                    <td className={className}>{id}</td>
                                    <td className={className}>
                                      <p className="flex">
                                        {scope.split(",").map((name, key) => (
                                          <Tooltip key={name} content={name}>
                                            <LinkIcon
                                              className={`cursor-pointer w-6 border-2 border-white rounded-full ${
                                                key === 0 ? "" : "-ml-2.5"
                                              }`}
                                            />
                                          </Tooltip>
                                        ))}
                                      </p>
                                    </td>
                                    <td className={className}>
                                      <Chip
                                        value={
                                          (power === 1 && "low") ||
                                          (power === 2 && "medium") ||
                                          (power === 3 && "high")
                                        }
                                        className="rounded-full w-fit"
                                        variant="ghost"
                                        color={
                                          (power === 1 && "green") ||
                                          (power === 2 && "orange") ||
                                          (power === 3 && "red")
                                        }
                                      />
                                    </td>
                                    <td className={className}>
                                      <div className="w-10/12">
                                        <Typography
                                          variant="small"
                                          className="mb-1 block text-xs font-medium text-blue-gray-600"
                                        >
                                          {completion}%
                                        </Typography>
                                        <Progress
                                          value={completion}
                                          variant="gradient"
                                          color={
                                            completion === 100
                                              ? "green"
                                              : "gray"
                                          }
                                          className="h-1"
                                        />
                                      </div>
                                    </td>
                                    <td className={className}>
                                      <Chip
                                        value={
                                          (triggered === true && "Y") ||
                                          (triggered === false && "N")
                                        }
                                        className="rounded-full w-fit"
                                        variant="ghost"
                                        color={
                                          (triggered === true && "green") ||
                                          (triggered === false && "orange")
                                        }
                                      />
                                    </td>
                                    <td className={className}>
                                      <Typography
                                        as="a"
                                        href="#"
                                        className="text-xs font-semibold text-blue-gray-600"
                                      >
                                        <EllipsisVerticalIcon
                                          strokeWidth={2}
                                          className="h-5 w-5 text-inherit"
                                        />
                                      </Typography>
                                    </td>
                                  </tr>
                                );
                              }
                            )}
                          </tbody>
                        </table>
                      </AccordionBody>
                    </Accordion>
                  );
                })}
              </CardBody>
            </Card>
          </div>
        </CardBody>
      </Card>
    </>
  );
}
