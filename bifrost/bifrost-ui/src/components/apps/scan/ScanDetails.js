import React from "react";
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
import Hosts from "./scandetails/Hosts";
import Vulnerabilities from "./scandetails/Vulnerabilities";

export default function ScanDetails() {
  const params = useParams();

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
                        <Tab value="hosts">Hosts</Tab>
                        <Tab value="vulnerabilities">Vulnerabilities</Tab>
                      </TabsHeader>
                      <TabsBody>
                        <TabPanel value="status">
                          <Status />
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
                    <ScanTimeline />
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
