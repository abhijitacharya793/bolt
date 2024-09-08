import {
  Collapse,
  Button,
  Card,
  Typography,
  CardBody
} from "@material-tailwind/react";
import React, { useEffect, useState } from "react";

export default function Apis({ scan_id }) {
  const [apis, setAPIs] = useState([]);
  const [enrichers, setEnrichers] = useState([]);
  // const [apiRequest, setApiRequest] = useState("");

  // const [openDetails, setOpenDetails] = useState({});
  // const toggleOpen = (index, api_id) => {
  //   getAPIRequest(api_id)
  //   setOpenDetails((prevState) => ({
  //     ...prevState,
  //     [index]: !prevState[index],
  //   }));
  // };

  const getEnrichers = (scan_id) => {
    fetch(`http://valhalla-api:8335/valhalla/v1/enricher/scan?id=${scan_id}`, {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => setEnrichers(data))
      .catch((err) => console.error(err));
  }

  const getAPI = (api_id) => {
    fetch(`http://bifrost-api:8333/bifrost/v1/api?id=${api_id}`, {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => setAPIs((prevAPIs) => [...prevAPIs, data]))
      .catch((err) => console.error(err));
  };

  // const getAPIRequest = (api_id) => {
  //   fetch(`http://bifrost-api:8333/bifrost/v1/api/request?id=${api_id}`, {
  //     method: "GET",
  //   })
  //     .then((res) => res.json())
  //     .then((data) => setApiRequest(data))
  //     .catch((err) => console.error(err));
  // };

  useEffect(() => {
    setAPIs([])
    console.log(`scan id: ${scan_id}`)
    getEnrichers(scan_id);
  }, [scan_id]);

  useEffect(() => {
    setAPIs([])
    if (enrichers.length > 0) {
      enrichers.forEach((enricher) => {
        console.log(`enricher: ${enricher.api_id}`);
        getAPI(enricher.api_id);
      });
    }
  }, [enrichers]);

  return (
    <>
      <div className="">
        <table className="w-full min-w-[640px] table-auto">
          <thead>
            <tr>
              {["Sr. No.", "Host", "Domain", "Status Code"].map((head) => (
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
            {apis && apis.map(({ id, target, rootDomain, domain, protocol, protocolVersion, port, method, path, body }, index) => {
              const isLast = index === 1;
              const classes = isLast
                ? "p-4"
                : "p-4 border-b border-blue-gray-50";

              return (
                <>
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
                        href={target}
                        target="_blank"
                      >
                        {target}
                      </a>
                    </td>
                    <td className={classes}>
                      <Typography
                        variant="small"
                        color="blue-gray"
                        className="font-normal"
                      >
                        {domain}
                      </Typography>
                    </td>
                    <td className={classes}>
                      <Typography
                        variant="small"
                        color="blue-gray"
                        className="font-normal"
                      >
                        {method}
                      </Typography>
                    </td>
                    {/* <td className={classes}>
                      <Button onClick={() => toggleOpen(index, id)}>Details</Button>
                    </td> */}
                  </tr>
                  {/* <tr>
                    <td colSpan={5}>
                      <Collapse open={openDetails[index]}>
                        <Card className="my-4 mx-auto w-8/12">
                          <CardBody>
                            <Typography variant="small" color="blue-gray" className="font-normal">
                              <strong>Request</strong> {apiRequest || "N/A"}
                            </Typography>
                          </CardBody>
                        </Card>
                      </Collapse>
                    </td>
                  </tr> */}
                </>
              );
            })}
          </tbody>
        </table>
      </div>
    </>
  );
}
