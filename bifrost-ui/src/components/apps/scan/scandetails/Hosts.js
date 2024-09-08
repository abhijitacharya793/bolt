import { Typography } from "@material-tailwind/react";
import React, { useEffect, useState } from "react";

export default function Hosts() {
  const [hosts, setHosts] = useState([]);

  const getHosts = () => {
    fetch("http://bifrost-api:8333/bifrost/v1/core/host", {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => setHosts(data))
      .catch((err) => console.error(err));
  };

  useEffect(() => {
    getHosts();
  }, []);

  return (
    <div className="">
      <table className="w-full min-w-[640px] table-auto">
        <thead>
          <tr>
            {["Sr. No.", "Host", "IP", "Status Code"].map((head) => (
              <th
                key={head}
                className="border-b border-blue-gray-50 py-3 px-5 text-left"
              >
                <Typography
                  variant="small"
                  className="text-[11px] font-bold uppercase text-blue-gray-400"
                >
                  {head}
                </Typography>
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {hosts.map(({ host, ip, status_code }, index) => {
            const isLast = index === 1;
            const classes = isLast ? "p-4" : "p-4 border-b border-blue-gray-50";

            return (
              <tr key={index}>
                <td className={classes}>
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="font-normal"
                  >
                    {index + 1}
                  </Typography>
                </td>
                <td className={classes}>
                  <a
                    className="font-normal text-sm underline"
                    href={host}
                    target="_blank"
                  >
                    {host}
                  </a>
                </td>
                <td className={classes}>
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="font-normal"
                  >
                    {ip}
                  </Typography>
                </td>
                <td className={classes}>
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="font-normal"
                  >
                    {status_code}
                  </Typography>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
