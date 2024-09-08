import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import {
  Accordion,
  AccordionHeader,
  AccordionBody,
  CardFooter,
} from "@material-tailwind/react";
import {
  Card,
  CardBody,
  CardHeader,
  Typography,
  Tabs,
  TabsHeader,
  Tab,
  Button,
} from "@material-tailwind/react";
import {
  QueueListIcon,
  GlobeAsiaAustraliaIcon,
  DevicePhoneMobileIcon,
  CloudIcon,
  BoltIcon,
} from "@heroicons/react/24/solid";
import no_results from "../../static/img/no_results.jpg";

import API from "./API";

export default function Asgard() {
  const [burpExport, setBurpExport] = useState({});
  const [scans, setScans] = useState({});
  const [toggle, setToggle] = React.useState([]);

  const handleClick = (key) => {
    let newArr = [...toggle];
    newArr[key] = toggle[key] === 0 ? 1 : 0;
    setToggle(newArr);
  };
  // rune
  const getExport = () => {
    fetch("http://rune-api:8334/rune/v1/burpExports", {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => {
        setBurpExport(data);
      })
      .catch((err) => console.error(err));
  };
  // valhalla
  const getScans = () => {
    fetch("http://valhalla-api:8335/valhalla/v1/enrichers", {
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
    getExport();
    getScans();
  }, []);

  let navigate = useNavigate();
  const navigateToScanDetails = (e) => {
    navigate(`/scans/scandetails/${e.target.name}`);
  };

  return (
    <>
      <div className="relative mt-8 h-20 w-full overflow-hidden rounded-xl bg-cover bg-center">
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
                <Typography
                  variant="h6"
                  color="blue-gray"
                  className="mb-1 uppercase"
                >
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
                {(Object.keys(scans).length > 0 &&
                  Object.keys(scans).map((scan_id, index) => {
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
                              {burpExport &&
                                burpExport[0] &&
                                burpExport.find(
                                  (item) => item.id === scan_id
                                ) &&
                                burpExport.find((item) => item.id === scan_id)[
                                  "name"
                                ]}
                              &nbsp;|&nbsp; This scan has&nbsp;
                              <p
                                className={` ${
                                  toggle[index] === 1
                                    ? "text-red-100"
                                    : "text-red-600"
                                }`}
                              >
                                {scans[scan_id].length}
                              </p>
                              &nbsp;api(s)
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
                                  "Id",
                                  "scope",
                                  "power",
                                  "method",
                                  "api",
                                  "completion",
                                  "status",
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
                                    status,
                                    api_id,
                                  },
                                  key
                                ) => {
                                  const className = `py-3 px-5 ${
                                    key === scans.length - 1
                                      ? ""
                                      : "border-b border-blue-gray-50"
                                  }`;
                                  return (
                                    <API
                                      className={className}
                                      id={id}
                                      scan_id={scan_id}
                                      scope={scope}
                                      power={power}
                                      completion={completion}
                                      tasks={tasks}
                                      status={status}
                                      api_id={api_id}
                                    />
                                  );
                                }
                              )}
                            </tbody>
                          </table>
                        </AccordionBody>
                      </Accordion>
                    );
                  })) || (
                  <div className="mx-2 px-2">
                    <div className="mb-12 grid gap-12 py-8 grid-cols-1 place-items-center">
                      <img src={no_results} className="w-96 h-96" />
                    </div>
                  </div>
                )}
              </CardBody>
            </Card>
          </div>
        </CardBody>
      </Card>
    </>
  );
}
