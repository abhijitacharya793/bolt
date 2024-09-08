import { CommandLineIcon } from "@heroicons/react/24/solid";
import { Typography } from "@material-tailwind/react";
import React from "react";

export default function MitmproxyLink() {
  return (
    <>
      <div className="flex items-center gap-6">
        <div className="rounded-lg blue border border-blue-gray-900 w-20 h-20 justify-center items-center flex">
          <CommandLineIcon fill="blue-gray" className="w-8 h-8" />
        </div>
        <div>
          <Typography variant="h6" color="blue-gray" className="mb-1 uppercase">
            Link Mitmproxy
          </Typography>
          <Typography
            variant="small"
            className="font-normal text-blue-gray-600"
          >
            Connect to Mitmproxy and get live feed in scope
          </Typography>
        </div>
      </div>
      <div className="grid-cols-1 mb-12 grid gap-12 px-4 py-8 lg:grid-cols-2 xl:grid-cols-3">
        link mitm
      </div>
    </>
  );
}
