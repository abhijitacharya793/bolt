import React from "react";

import {
  Card,
  CardBody,
  Typography,
  Tabs,
  TabsHeader,
  Tab,
  TabsBody,
  TabPanel,
} from "@material-tailwind/react";
import {
  FolderArrowDownIcon,
  CommandLineIcon,
  LinkIcon,
  AdjustmentsHorizontalIcon,
} from "@heroicons/react/24/solid";
import BurpsuiteExport from "./adaptor/BurpsuiteExport";
import MitmproxyLink from "./adaptor/MitmproxyLink";
import BurpsuiteLink from "./adaptor/BurpsuiteLink";
import Manual from "./adaptor/Manual";

export default function Inputs() {
  return (
    <>
      <div className="relative mt-8 h-20 w-full overflow-hidden rounded-xl bg-cover bg-center">
        <div className="absolute inset-0 h-full w-full bg-orange-100" />
      </div>
      <Card className="mx-3 -mt-16 mb-6 lg:mx-4 border border-blue-gray-100">
        <CardBody className="p-4">
          <Tabs value="burpexport">
            <div className="mb-10 flex items-center justify-between flex-wrap gap-6">
              <div className="flex items-center gap-6"></div>
              <div className="w-full px-40">
                <TabsHeader>
                  <Tab value="burpexport">
                    <FolderArrowDownIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                    Burpsuite Export
                  </Tab>
                  <Tab value="mitmlink">
                    <CommandLineIcon className="-mt-0.5 mr-2 inline-block h-5 w-5" />
                    Link Mitmproxy
                  </Tab>
                  <Tab value="burplink">
                    <LinkIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                    Link Burpsuite
                  </Tab>
                  <Tab value="manual">
                    <AdjustmentsHorizontalIcon className="-mt-1 mr-2 inline-block h-5 w-5" />
                    Manual Configuration
                  </Tab>
                </TabsHeader>
              </div>
            </div>
            <TabsBody className="!overflow-x-hidden !overflow-y-visible">
              <TabPanel key="burpexport" value="burpexport">
                <BurpsuiteExport />
              </TabPanel>
              <TabPanel key="mitmlink" value="mitmlink">
                <MitmproxyLink />
              </TabPanel>
              <TabPanel key="burplink" value="burplink">
                <BurpsuiteLink />
              </TabPanel>
              <TabPanel key="manual" value="manual">
                <Manual />
              </TabPanel>
            </TabsBody>
            <div className="px-4 pb-4"></div>
          </Tabs>
        </CardBody>
      </Card>
    </>
  );
}
