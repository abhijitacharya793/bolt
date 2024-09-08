import React, { useEffect, useState } from "react";
import { useParams } from "react-router";

import {
  Card,
  CardBody,
  CardHeader,
  Typography,
  Switch,
  Tabs,
  TabsHeader,
  Tab,
  TabsBody,
  TabPanel,
} from "@material-tailwind/react";
import { QueueListIcon } from "@heroicons/react/24/solid";
import ScanTimeline from "./ScanTimeline";
import Status from "./scandetails/Status";
import Apis from "./scandetails/Apis";
import Hosts from "./scandetails/Hosts";
import Vulnerabilities from "./scandetails/Vulnerabilities";

export default function ScanDetails() {
  const params = useParams();

  const [scanDetails, setScanDetails] = useState([]);

  const getScanDetails = (id) => {
    fetch(`http://valhalla-api:8335/valhalla/v1/enricher/scan?id=${id}`, {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => {
        setScanDetails(data);
      })
      .catch((err) => console.error(err));
  };

  useEffect(() => {
    getScanDetails(params["id"]);
  }, []);

  const calculateCompletition = () => {
    let total = 0;
    for (let obj of scanDetails) {
      total += obj["completion"];
    }
    return total / scanDetails.length;
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
                  Scan Details
                </Typography>
                <Typography
                  variant="small"
                  className="font-normal text-blue-gray-600"
                >
                  Get an in-depth understanding of the scan.
                </Typography>
              </div>
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
                <div className="grid grid-cols-6 gap-4">
                  <div className="col-span-4 p-4">
                    <Tabs value="status">
                      <TabsHeader className="w-1/2">
                        <Tab value="status">Status</Tab>
                        <Tab value="api">API</Tab>
                        <Tab value="hosts">Hosts</Tab>
                        <Tab value="vulnerabilities">Vulnerabilities</Tab>
                      </TabsHeader>
                      <TabsBody>
                        <TabPanel value="status">
                          {(calculateCompletition() !== 100 && (
                            <div className="h-96 px-8">
                              <div className="flex items-center justify-center pt-32 pb-10">
                                <svg
                                  class="animate-spin -ml-1 mr-3 h-5 w-5 text-black"
                                  xmlns="http://www.w3.org/2000/svg"
                                  fill="none"
                                  viewBox="0 0 24 24"
                                >
                                  <circle
                                    class="opacity-25"
                                    cx="12"
                                    cy="12"
                                    r="10"
                                    stroke="currentColor"
                                    stroke-width="4"
                                  ></circle>
                                  <path
                                    class="opacity-75"
                                    fill="currentColor"
                                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                                  ></path>
                                </svg>
                                <h1 className="uppercase text-black">
                                  Scan in progress
                                </h1>
                              </div>
                              <div>
                                <div className="progress-bar">
                                  <div
                                    className="progress"
                                    style={{
                                      width: `${calculateCompletition()}%`,
                                    }}
                                  ></div>
                                </div>
                              </div>
                            </div>
                          )) || <Status />}
                        </TabPanel>
                        <TabPanel value="api">
                          <Apis scan_id={params["id"]} />
                        </TabPanel>
                        <TabPanel value="hosts">
                          <Hosts />
                        </TabPanel>
                        <TabPanel value="vulnerabilities">
                          <Vulnerabilities />
                        </TabPanel>
                      </TabsBody>
                    </Tabs>
                  </div>
                  <div className="col-span-2 p-4">
                    <ScanTimeline scanDetails={scanDetails} />
                  </div>
                </div>
              </CardBody>
            </Card>
          </div>
        </CardBody>
      </Card>
    </>
  );
}
