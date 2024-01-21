import React from "react";
import {
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
      <Card className={`border ${border} shadow-lg ${background}`}>
        <CardHeader
          variant="gradient"
          color="gray"
          floated={false}
          shadow={false}
          className="absolute grid h-12 w-12 place-items-center"
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
        <CardFooter className="border-t border-blue-gray-50 p-4">
          <span
            className={(change === "+" && "text-green-500") || "text-red-500"}
          >
            {change}
            {change_value}
          </span>{" "}
          than last week
        </CardFooter>
      </Card>
    </>
  );
}
