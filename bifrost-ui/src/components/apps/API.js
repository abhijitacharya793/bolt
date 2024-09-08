import React, { useState, useEffect } from "react";
import { Typography, Tooltip, Progress, Chip } from "@material-tailwind/react";
import { EllipsisVerticalIcon, LinkIcon } from "@heroicons/react/24/solid";

export default function API({
  className,
  id,
  scan_id,
  scope,
  power,
  completion,
  tasks,
  status,
  api_id,
}) {
  const [api, setAPI] = useState({});
  // bifrost
  const getAPI = (api_id) => {
    fetch(`http://bifrost-api:8333/bifrost/v1/api?id=${api_id}`, {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => {
        setAPI(data);
      })
      .catch((err) => console.error(err));
  };

  useEffect(() => {
    getAPI(api_id);
  }, []);

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
            (power === "1" && "low") ||
            (power === "2" && "medium") ||
            (power === "3" && "high")
          }
          className="rounded-full w-fit"
          variant="ghost"
          color={
            (power === "1" && "green") ||
            (power === "2" && "orange") ||
            (power === "3" && "red")
          }
        />
      </td>
      <td className={className}>
        <Chip
          value={api["method"]}
          className="rounded-full w-fit"
          variant="ghost"
          color={
            (api["method"] === "GET" && "green") ||
            (api["method"] === "POST" && "yellow") ||
            (api["method"] === "PUT" && "blue") ||
            (api["method"] === "DEL" && "red")
          }
        />
      </td>
      <td className={`underline text-blue-300 ${className}`}>
        <a target="_blank" href={api["target"]}>
          {api["path"]}
        </a>
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
            color={completion === 100 ? "green" : "gray"}
            className="h-1"
          />
        </div>
      </td>
      <td className={className}>
        <Chip
          value={
            (status === "1" && "Queued") ||
            (status === "2" && "Running") ||
            (status === "3" && "Successful") ||
            (status === "4" && "Failed")
          }
          className="rounded-full w-fit"
          variant="ghost"
          color={
            (status === "1" && "grey") ||
            (status === "2" && "orange") ||
            (status === "3" && "green") ||
            (status === "4" && "red")
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
