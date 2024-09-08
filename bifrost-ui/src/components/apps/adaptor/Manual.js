import { AdjustmentsHorizontalIcon, LinkIcon } from "@heroicons/react/24/solid";
import { Typography } from "@material-tailwind/react";
import React from "react";

export default function Manual() {
  return (
    <>
      <div className="flex items-center gap-6">
        <div className="rounded-lg blue border border-blue-gray-900 w-20 h-20 justify-center items-center flex">
          <AdjustmentsHorizontalIcon fill="blue-gray" className="w-8 h-8" />
        </div>
        <div>
          <Typography variant="h6" color="blue-gray" className="mb-1 uppercase">
            Manual Configuration
          </Typography>
          <Typography
            variant="small"
            className="font-normal text-blue-gray-600"
          >
            Customize every part of your scan
          </Typography>
        </div>
      </div>
      <div className="grid-cols-1 mb-12 grid gap-12 px-4 py-8 lg:grid-cols-2 xl:grid-cols-3">
        Manual
      </div>
    </>
  );
}
