import React from "react";
import {
  Chip,
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  Typography,
} from "@material-tailwind/react";

export default function StatisticsCard({
  icon,
  entry,
  entry_value,
  change,
  change_value,
  change_text,
  background,
  border,
}) {
  var footer = {
    color: "text-green-500",
    value: "+3%",
    label: "than last month",
  };
  return (
    <>
      <Card
        className={`border border-blue-gray-100 transition-transform transform hover:scale-105`}
      >
        <CardHeader
          variant="gradient"
          color="gray"
          floated={false}
          shadow={false}
          className="absolute grid h-12 w-12 place-items-center rounded-full"
        >
          {icon}
        </CardHeader>
        <CardBody className="p-4 text-right">
          <Typography
            variant="small"
            className="font-normal text-blue-gray-600"
          >
            {entry}
          </Typography>
          <Typography variant="h4" color="blue-gray">
            {entry_value}
          </Typography>
        </CardBody>
        <CardFooter className="border-t border-blue-gray-100 p-4">
          <div className="flex gap-2">
            <Chip
              variant="ghost"
              color={(change === "+" && "green") || "red"}
              value={change + change_value}
            />{" "}
            {change_text}
          </div>
        </CardFooter>
      </Card>
    </>
  );
}
